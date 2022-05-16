import requests

from cocksearcher.infrastructures.dto.cocktail_db import CocktailData

BASE_URL = "https://www.thecocktaildb.com/api/json/v1/1/search.php"


def get_cocktail_list_by_alphabet(alphabet: str) -> list[CocktailData]:
    response = requests.get(BASE_URL, params=dict(f=alphabet))
    data = response.json()
    drinks = data["drinks"]

    if drinks is None:
        return []

    return [CocktailData.from_json(drink) for drink in drinks]


def get_cocktail_list() -> list[CocktailData]:
    cocktail_list = []

    for letter in (chr(i) for i in range(97, 122)):
        cocktail_list.extend(get_cocktail_list_by_alphabet(letter))

    return cocktail_list
