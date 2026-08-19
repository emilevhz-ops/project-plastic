from fastapi import FastAPI

from api.routes import health

app = FastAPI(title="Emile Plastic API")

app.include_router(health.router)
