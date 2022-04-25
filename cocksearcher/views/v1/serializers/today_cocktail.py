import dataclasses
from dataclasses import dataclass
from typing import Dict, List, Tuple, Type

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

    is_liked = serializers.BooleanField(allow_null=False)

    def validate(self, data: Dict[str, str]) -> TodayCocktailQuery:
        fields = TodayCocktailQuery.get_keys_info()

        if fields not in data.keys():
            raise ValidationError('field is must be empty')

        for key in fields:
            if not data[key].isnumeric():
                raise ValidationError('field is must be number')

        return TodayCocktailQuery.from_query_string(data)
