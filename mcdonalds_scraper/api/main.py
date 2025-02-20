from typing import Any

from fastapi import FastAPI

from api.crud import get_product_by_name
from api.schemas import MenuItemSchema
from api.utils import MenuDataLoader
from mcdonalds_scraper.settings import FEED_URI

loader = MenuDataLoader(file_path=FEED_URI)
menu_data = loader.get_menu_data()

app = FastAPI()


@app.get("/products/", response_model=list[MenuItemSchema])
def read_products():
    return menu_data


@app.get("/products/{product_name}/", response_model=MenuItemSchema)
def read_product(product_name: str) -> MenuItemSchema:
    return get_product_by_name(product_name, menu_data)


@app.get("/products/{product_name}/{product_field}/")
def read_product_field(product_name: str, product_field: str) -> Any:
    product = get_product_by_name(product_name, menu_data)
    return getattr(product, product_field, None)
