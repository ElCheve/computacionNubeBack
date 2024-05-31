from fastapi import APIRouter, HTTPException
from schemas.product import ProductCreate, Product
from services.product_service import create_product, get_products
from typing import List

router = APIRouter()

@router.post("/", response_model=Product)
def add_product(product: ProductCreate):
    return create_product(product)

@router.get("/", response_model=List[Product])
def read_products():
    products = get_products()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products
