from drf_spectacular.utils import OpenApiParameter

from cocksearcher.views.v1.schemas import OPENAPI_TYPES
from cocksearcher.views.v1.serializers.today_cocktail import TodayCocktailQuery

today_cocktail_params = [
    OpenApiParameter(
        name=key,
        type=OPENAPI_TYPES[value_type],
        location=OpenApiParameter.QUERY,
    ) for key, value_type in TodayCocktailQuery.get_keys_info()
]
