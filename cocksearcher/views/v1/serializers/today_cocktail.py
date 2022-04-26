from dataclasses import dataclass
from typing import Dict

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from cocksearcher.views.v1.requests.base_query import BaseQuery


@dataclass(frozen=True)
class TodayCocktailQuery(BaseQuery):
    sad: int
    angry: int
    happy: int
    exciting: int
    hungry: int

    @staticmethod
    def from_query_string(data):
        return TodayCocktailQuery(
            sad=data['sad'],
            angry=data['angry'],
            happy=data['happy'],
            exciting=data['exciting'],
            hungry=data['hungry']
        )


class TodayCocktailSerializer(serializers.Serializer):
    name = serializers.CharField(allow_null=False)
    ingredients = serializers.ListField(child=serializers.CharField(allow_null=False))
    recipe = serializers.ListField(child=serializers.CharField(allow_null=False))
    mood = serializers.CharField(allow_null=False)
    abv = serializers.FloatField(allow_null=False)
    likes = serializers.CharField(allow_null=False)
    is_liked = serializers.BooleanField(allow_null=False)

    def validate(self, data: Dict[str, str]) -> TodayCocktailQuery:
        fields = TodayCocktailQuery.get_keys_info()

        if fields not in data.keys():
            raise ValidationError('field is must be empty')

        for key in fields:
            if not data[key].isnumeric():
                raise ValidationError('field is must be number')

        return TodayCocktailQuery.from_query_string(data)
