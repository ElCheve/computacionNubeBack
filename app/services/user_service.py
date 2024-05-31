from core.config import settings
from core.security import hash_password, verify_password
from supabase import create_client, Client
from schemas.user import UserCreate, UserLogin

supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

def create_user(user: UserCreate):
    hashed_password = hash_password(user.password)
    response = supabase.table('users').insert({
        "username": user.username,
        "password": hashed_password
    }).execute()
    return response.data

def authenticate_user(user: UserLogin):
    response = supabase.table('users').select("*").eq("username", user.username).execute()
    if response.data and verify_password(user.password, response.data[0]['password']):
        return "some_generated_token"  # Aquí deberías generar un JWT o similar
    return None
