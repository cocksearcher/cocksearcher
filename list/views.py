from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from cocksearcher.infrastructures.cockdb.cockdb import get_cocktail_list
from cocksearcher.infrastructures.elasticsearch.cocktail import CocktailESRepository
from list.params import cocktail_list_params
from list.serializers import CocktailListSerializer


class CocktailListView(APIView):
    serializer_class = CocktailListSerializer

    @extend_schema(
        operation_id="cocksearcher-list",
        tags=["cocksearcher"],
        parameters=cocktail_list_params
    )
    def get(self, request: Request):
        pass


class CocktailListRefreshView(APIView):
    cocktail_repository = CocktailESRepository()

    @extend_schema(
        operation_id="cocksearcher-list-refresh",
        tags=["cocksearcher", "refresh"],
    )
    def post(self, _: Request):
        cocktails = get_cocktail_list()
        self.cocktail_repository.insert_all(cocktails)

        return Response(status=status.HTTP_200_OK, data={"message": "Cocktail list refreshing is successfully "
                                                                    "completed."})