from dataclasses import dataclass
from enum import Enum
from typing import Dict, Any

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from cocksearcher.views.v1.requests.base_query import BaseQuery
from cocksearcher.views.v1.serializers.cocktail_detail import CocktailDetailSerializer


class Sort(Enum):
    Asc = True
    Desc = False


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
            alphabet_type: Sort = sort_type[data['alphabet']]
            abv_type: Sort = sort_type[data['abv']]

        except KeyError:
            raise ValidationError("alphabet or abv value must be in asc, desc")

        return CocktailListQuery(
            name=data['name'],
            topic=data['topic'],
            alphabet=alphabet_type,
            abv=abv_type
        )


class CocktailListSerializer(serializers.Serializer):
    data = serializers.ListField(child=CocktailDetailSerializer(), required=True)
