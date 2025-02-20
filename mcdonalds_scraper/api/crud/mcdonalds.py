from fastapi import HTTPException, status

from api.schemas import MenuItemSchema


def get_product_by_name(
    product_name: str, products_data: dict
) -> MenuItemSchema:
    for product in products_data:
        if product.get("name").lower() == product_name.lower():
            return MenuItemSchema(**product)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with name {product_name} not found",
    )
