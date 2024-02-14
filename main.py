from fastapi import FastAPI
from routes.route_agencia import agencia_router
from routes.route_rodoviario import rodoviario_router

app = FastAPI()

app.include_router(agencia_router)
app.include_router(rodoviario_router)
