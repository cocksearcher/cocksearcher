from drf_spectacular.utils import extend_schema
from rest_framework.request import Request
from rest_framework.views import APIView

from cocksearcher.views.v1.schemas.today_cocktail import today_cocktail_params
from cocksearcher.views.v1.serializers.today_cocktail import TodayCocktailSerializer


class TodayCocktailView(APIView):

    serializer_class = TodayCocktailSerializer

    @extend_schema(
        tags=["칵테일"],
        parameters=today_cocktail_params
    )
    def get(self, request: Request):
        query_params = request.query_params

        serializer = self.serializer_class(data=query_params)
        serializer.validate()