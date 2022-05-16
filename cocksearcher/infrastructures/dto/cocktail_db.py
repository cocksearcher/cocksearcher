from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class CocktailData:
    id: int
    name: str
    tags: list[str]
    category: str
    alcoholic: str
    glass: str
    instruction: Instruction
    ingredients: list[str]
    measures: list[str]
    modified_at: datetime
    image_location: ImageLocation

    @staticmethod
    def from_json(data: any) -> CocktailData:
        return CocktailData(
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


@dataclass(frozen=True)
class Instruction:
    default: str
    de: str
    fr: str
    it: str


@dataclass(frozen=True)
class ImageLocation:
    drink_thumbnail_url: str
    image_source: str
    image_attribution: str
