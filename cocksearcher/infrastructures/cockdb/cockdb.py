import requests

from cocksearcher.domain.cocktail import Cocktail, Instruction, ImageLocation

BASE_URL = "https://www.thecocktaildb.com/api/json/v1/1/search.php"


def get_cocktail_from_json(data: any):
    return Cocktail(
        id=data['idDrink'],
        name=data['strDrink'],
        tags=str(data['strTags']).split(sep=','),
        category=data['strCategory'],
        alcoholic=data['strAlcoholic'],
        glass=data['strGlass'],
        instruction=Instruction(
            default=data['strInstructions'],
            de=data['strInstructionsDE'],
            fr=data['strInstructionsFR'],
            it=data['strInstructionsIT']
        ),
        ingredients=[data[f"strIngredient{i}"] for i in range(1, 16) if data[f"strIngredient{i}"] is not None],
        measures=[data[f"strMeasure{i}"] for i in range(1, 16) if data[f"strMeasure{i}"] is not None],
        modified_at=data["dateModified"],
        image_location=ImageLocation(
            drink_thumbnail_url=data["strDrinkThumb"],
            image_source=data["strImageSource"],
            image_attribution=data["strImageAttribution"]
        )
    )


def get_cocktail_list_by_alphabet(alphabet: str) -> list[Cocktail]:
    response = requests.get(BASE_URL, params=dict(f=alphabet))
    data = response.json()
    drinks = data["drinks"]

    if drinks is None:
        return []

    return [get_cocktail_from_json(drink) for drink in drinks]


def get_cocktail_list() -> list[Cocktail]:
    cocktail_list = []

    for letter in (chr(i) for i in range(97, 122)):
        cocktail_list.extend(get_cocktail_list_by_alphabet(letter))

    return cocktail_list
