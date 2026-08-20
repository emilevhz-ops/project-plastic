from fastapi import FastAPI

from api.routes import auth, health

app = FastAPI(title="Emile Plastic API")

app.include_router(health.router)
app.include_router(auth.router)
