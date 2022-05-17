from drf_spectacular.utils import extend_schema
from rest_framework.request import Request
from rest_framework.views import APIView

from cocksearcher.views.v1.schemas.params import cocktail_list_params
from cocksearcher.views.v1.serializers.cocktail_list import CocktailListSerializer


class CocktailListView(APIView):
    serializer_class = CocktailListSerializer

    @extend_schema(
        operation_id="cocktail-list",
        tags=["cocktail"],
        parameters=cocktail_list_params
    )
    def get(self, request: Request):
        pass

    @extend_schema(
        operation_id="cocktail-list-refresh",
        tags=["cocktail", "refresh"],
    )
    def post(self, request: Request):
        pass
