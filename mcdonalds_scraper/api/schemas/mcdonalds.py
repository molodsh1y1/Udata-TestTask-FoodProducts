from typing import Any

from pydantic import BaseModel


class MenuItemSchema(BaseModel):
    name: str
    description: str | None
    calories: int | None
    fats: float | None
    carbs: float | None
    proteins: float | None
    unsaturated_fats: float | None
    sugar: float | None
    salt: float | None
    portion: int | None


class ProductFieldResponseSchema(BaseModel):
    value: Any
