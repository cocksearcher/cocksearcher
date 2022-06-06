import asyncio

import aiohttp

from cocksearcher.domain.cocktail import Cocktail, Instruction, ImageLocation

BASE_URL = "https://www.thecocktaildb.com/api/json/v1/1/search.php"


async def get_cocktail_from_json(data: any):
    return Cocktail(
        id=data['idDrink'],
        name=data['strDrink'],
        tags=str(data['strTags']).split(sep=','),
        category=data['strCategory'],
        alcoholic=data['strAlcoholic'],
        glass=data['strGlass'],
        instruction=Instruction(
            default=data['strInstructions'],
            de=data['strInstructionsDE'],
            fr=data['strInstructionsFR'],
            it=data['strInstructionsIT']
        ),
        ingredients=[data[f"strIngredient{i}"] for i in range(1, 16) if data[f"strIngredient{i}"] is not None],
        measures=[data[f"strMeasure{i}"] for i in range(1, 16) if data[f"strMeasure{i}"] is not None],
        modified_at=data["dateModified"],
        image_location=ImageLocation(
            drink_thumbnail_url=data["strDrinkThumb"],
            image_source=data["strImageSource"],
            image_attribution=data["strImageAttribution"]
        )
    )


async def get_cocktail_list_by_alphabet(alphabet: str) -> list[Cocktail]:
    async with aiohttp.ClientSession() as session:
        response = await session.get(BASE_URL, params=dict(f=alphabet))
        data = await response.json()

        drinks = data["drinks"]

        if drinks is None:
            return []

        return [await get_cocktail_from_json(drink) for drink in drinks]


async def _get_cocktail_list() -> list[Cocktail]:
    results = []
    jobs = [get_cocktail_list_by_alphabet(chr(i)) for i in range(97, 122)]

    for datas in await asyncio.gather(*jobs):
        results.extend(datas)

    return results


def get_cocktail_list() -> list[Cocktail]:
    return asyncio.run(_get_cocktail_list())
