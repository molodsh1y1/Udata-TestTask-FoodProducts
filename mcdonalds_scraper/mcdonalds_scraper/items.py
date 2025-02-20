# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass


@dataclass
class McDonaldMenuItem:
    name: str
    description: str
    calories: int
    fats: float
    carbs: float
    proteins: float
    unsaturated_fats: float
    sugar: float
    salt: float
    portion: int
