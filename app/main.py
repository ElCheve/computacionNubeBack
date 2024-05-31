from fastapi import FastAPI
from api.v1.endpoints import login, products
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(login.router, prefix="/api/v1/login", tags=["login"])
app.include_router(products.router, prefix="/api/v1/products", tags=["products"])

origins = [
    "http://localhost",
    "http://127.0.0.1:8000",  # Ajusta el puerto según sea necesario
    "http://127.0.0.1:8001",  # Ajusta el puerto según sea necesario
    # Agrega más orígenes según sea necesario
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)