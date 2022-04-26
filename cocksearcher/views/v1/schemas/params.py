from drf_spectacular.utils import OpenApiParameter

from cocksearcher.views.v1.schemas import OPENAPI_TYPES
from cocksearcher.views.v1.serializers.cocktail_list import CocktailListQuery
from cocksearcher.views.v1.serializers.today_cocktail import TodayCocktailQuery

today_cocktail_params = [
    OpenApiParameter(
        name=key,
        type=OPENAPI_TYPES[value_type],
        location=OpenApiParameter.QUERY,
    ) for key, value_type in TodayCocktailQuery.get_keys_info()
]

cocktail_list_params = [
    OpenApiParameter(
        name=key,
        type=OPENAPI_TYPES[value_type],
        location=OpenApiParameter.QUERY,
    ) for key, value_type in CocktailListQuery.get_keys_info()
]
