import requests

BASE_URL = "www.thecocktaildb.com/api/json/v1/1/search.php"


def get_cocktail_list_by_alphabet(alphabet: str):
    response = requests.get(BASE_URL, params=dict(f=alphabet))
    response.json()


def get_cocktail_list():
    # loop by ascii letters
    for letter in (chr(i) for i in range(97, 122)):
        get_cocktail_list_by_alphabet(letter)
