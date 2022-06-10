from drf_spectacular.types import OpenApiTypes

from cocksearcher.serializers import Sort

OPENAPI_TYPES = {
    int: OpenApiTypes.NUMBER,
    str: OpenApiTypes.STR,
    Sort: OpenApiTypes.STR
}
