from dataclasses import dataclass
from typing import Dict, Any

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from cocksearcher.base_query import BaseQuery
from cocksearcher.serializers import Sort
from cocktail.serializers import CocktailDetailSerializer


@dataclass(frozen=True)
class CocktailListQuery(BaseQuery):
    name: str
    topic: str
    alphabet: Sort
    abv: Sort

    @staticmethod
    def from_query_string(data: Dict[str, Any]):
        try:
            sort_type = {
                "asc": Sort.Asc,
                "desc": Sort.Desc
            }
            alphabet_type: Sort = sort_type[data.get("alphabet", "asc")]
            abv_type: Sort = sort_type[data.get("abv", "asc")]

        except KeyError:
            raise ValidationError("alphabet or abv value must be in asc, desc")

        return CocktailListQuery(
            name=data.get("name", ""),
            topic=data.get("topic", ""),
            alphabet=alphabet_type,
            abv=abv_type
        )


class CocktailListSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    data = serializers.ListField(child=CocktailDetailSerializer(), required=True)
