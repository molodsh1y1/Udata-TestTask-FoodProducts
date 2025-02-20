from typing import Any

from fastapi import FastAPI

from api.crud import get_product_by_name
from api.schemas import MenuItemSchema
from api.utils import MenuDataLoader
from mcdonalds_scraper.settings import FEED_URI

loader = MenuDataLoader(file_path=FEED_URI)
menu_data = loader.get_menu_data()

app = FastAPI()


@app.get(
    "/products/",
    response_model=list[MenuItemSchema],
    description="Get all products from the menu",
    responses={
        200: {
            "description": "List of all products",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "name": "Фіш Рол",
                            "description": (
                                "Свіжий смак овочів у поєднанні з соковитим філе риби в паніруванні. "
                                "Страва для справжніх гурманів!"
                            ),
                            "calories": 436,
                            "fats": 19,
                            "carbs": 46,
                            "proteins": 18,
                            "unsaturated_fats": 3.34,
                            "sugar": 3.93,
                            "salt": 1.4,
                            "portion": 190
                        },
                        {
                            "name": "МакТост із сиром",
                            "description": "Гаряча булочка з двома скибочками сиру “Чеддер”.",
                            "calories": 264,
                            "fats": 10.1,
                            "carbs": 33,
                            "proteins": 10.4,
                            "unsaturated_fats": 5.2,
                            "sugar": 5.2,
                            "salt": 1.6,
                            "portion": 73
                        },
                    ]
                }
            },
        }
    }
)
def read_products():
    return menu_data


@app.get(
    "/products/{product_name}/",
    response_model=MenuItemSchema,
    description="Get product by name",
    responses={
        200: {
            "description": "Product details",
            "content": {
                "application/json": {
                    "example": {
                        "name": "Фіш Рол",
                        "description": (
                            "Свіжий смак овочів у поєднанні з соковитим філе риби в паніруванні. "
                            "Страва для справжніх гурманів!"
                        ),
                        "calories": 436,
                        "fats": 19,
                        "carbs": 46,
                        "proteins": 18,
                        "unsaturated_fats": 3.34,
                        "sugar": 3.93,
                        "salt": 1.4,
                        "portion": 190
                    }
                }
            },
        },
        404: {
            "description": "Product not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Product not found"
                    }
                }
            }
        }
    }
)
def read_product(product_name: str) -> MenuItemSchema:
    return get_product_by_name(product_name, menu_data)


@app.get(
    "/products/{product_name}/{product_field}/",
    description="Get product field by name",
    responses={
        200: {
            "description": "Product field value",
            "content": {
                "application/json": {
                    "example": 436
                }
            },
        },
        404: {
            "description": "Product not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Product not found"
                    }
                }
            }
        }
    }
)
def read_product_field(product_name: str, product_field: str) -> Any:
    product = get_product_by_name(product_name, menu_data)
    return getattr(product, product_field, None)
