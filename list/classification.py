import asyncio

import aiohttp
import logging

import numpy as np
from cv2 import cv2
from sklearn.cluster import KMeans

import numpy

from cocksearcher.infrastructures.cockdb.cocktail import Cocktail, ImageLocation

logger = logging.getLogger(__name__)


async def _extract_primary_color_in_image(image_stream: bytes) -> list[float]:
    np_image = np.frombuffer(image_stream, numpy.uint8)
    cv_image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)
    image: numpy.ndarray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    clt = KMeans(n_clusters=5)
    clt.fit(image)
    c_labels = numpy.arange(0, len(numpy.unique(clt.labels_)) + 1)
    (c_hist, _) = numpy.histogram(clt.labels_, bins=c_labels)
    c_hist = c_hist.astype("float")
    c_hist /= c_hist.sum()

    for percent, color in zip(c_hist, clt.cluster_centers_):
        if 30 < percent < 40:
            return color

    return clt.cluster_centers_[0]


async def _classification_by_image_url(cocktail: Cocktail) -> Cocktail:
    async with aiohttp.ClientSession() as session:
        async with session.get(cocktail.image_location.drink_thumbnail_url) as resp:
            if resp.status != 200:
                logger.error(f"image request failed. (url={cocktail.image_location.drink_thumbnail_url})")
                return cocktail
            extracted_color = await _extract_primary_color_in_image(await resp.content.read())


async def _classification_images(cocktails: list[Cocktail]):
    jobs = [_classification_by_image_url(cocktail) for cocktail in cocktails]

    return await asyncio.gather(*jobs)


def classification_images(cocktails: list[Cocktail]):
    return asyncio.run(_classification_images(cocktails=cocktails))


classification_images([(Cocktail(image_location=ImageLocation(drink_thumbnail_url="https://www.thecocktaildb.com"
                                                                                  "/images/media/drink "
                                                                                  "/nkwr4c1606770558.jpg")))])
