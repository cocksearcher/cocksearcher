from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from cocktail.serializers import CocktailDetailSerializer, CocktailPreferSerializer


class CocktailDetailView(APIView):
    serializer_class = CocktailDetailSerializer

    @extend_schema(
        operation_id="item-cocktail",
        tags=["cocktail"],
        parameters=[OpenApiParameter(
            name="id",
            type=OpenApiTypes.NUMBER,
            location=OpenApiParameter.PATH
        )]
    )
    def get(self, request, item_id: int):
        if item_id is None:
            raise NotFound("item is not found")

        return Response()


class CocktailPreferView(APIView):

    serializer_class = CocktailPreferSerializer

    @extend_schema(
        operation_id="cocktail-prefer",
        tags=["cocktail"],
        parameters=[OpenApiParameter(
            name="item_id",
            type=OpenApiTypes.NUMBER,
            location=OpenApiParameter.PATH
        )]
    )
    def post(self, request, item_id: int):
        if item_id is None:
            raise NotFound("cocktail is not found")

        return Response()
