from drf_spectacular.types import OpenApiTypes

from cocksearcher.views.v1.serializers.cocktail_list import Sort

OPENAPI_TYPES = {
    int: OpenApiTypes.NUMBER,
    str: OpenApiTypes.STR,
    Sort: OpenApiTypes.STR
}
