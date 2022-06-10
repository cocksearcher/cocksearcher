from drf_spectacular.utils import OpenApiParameter

from cocksearcher.openapi_types import OPENAPI_TYPES
from today.serializers import TodayCocktailQuery

today_cocktail_params = [
    OpenApiParameter(
        name=key,
        type=OPENAPI_TYPES[value_type],
        location=OpenApiParameter.QUERY,
    ) for key, value_type in TodayCocktailQuery.get_keys_info()
]
