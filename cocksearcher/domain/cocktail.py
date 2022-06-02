from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Cocktail:
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
