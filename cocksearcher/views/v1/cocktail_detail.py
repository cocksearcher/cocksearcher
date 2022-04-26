from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from cocksearcher.views.v1.serializers.cocktail_detail import CocktailDetailSerializer


class CocktailDetailView(APIView):
    serializer_class = CocktailDetailSerializer

    @extend_schema(
        operation_id="item-detail",
        tags=["cocktail"],
        parameters=[OpenApiParameter(
            name="item_id",
            type=OpenApiTypes.NUMBER,
            location=OpenApiParameter.PATH
        )]
    )
    def get(self, item_id: int):
        if item_id is None:
            raise NotFound("item is not found")
