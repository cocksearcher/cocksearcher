from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from cocksearcher.views.v1.serializers.cocktail_prefer import CocktailPreferSerializer


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
    def post(self, id: int):
        if id is None:
            raise NotFound("cocktail is not found")
