from core.config import settings
from supabase import create_client, Client
from schemas.product import ProductCreate

supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

def create_product(product: ProductCreate):
    response = supabase.table('seafood_products').insert({
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock
    }).execute()
    return response.data

def get_products():
    response = supabase.table('seafood_products').select("*").execute()
    return response.data
