from drf_spectacular.utils import OpenApiParameter

from cocksearcher.openapi_types import OPENAPI_TYPES
from list.serializers import CocktailListQuery

cocktail_list_params = [
    OpenApiParameter(
        name=key,
        type=OPENAPI_TYPES[value_type],
        location=OpenApiParameter.QUERY,
    ) for key, value_type in CocktailListQuery.get_keys_info()
]
