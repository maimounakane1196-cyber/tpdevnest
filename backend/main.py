import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text

app = FastAPI()

# CORS : autorise le frontend (autre port) à appeler le backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Adresse de la base PostgreSQL (lue dans une variable d'environnement)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://user:password@db:5432/tpdb")
engine = create_engine(DATABASE_URL)  # ne se connecte pas encore


@app.get("/health")
def health():
    # Route simple : sert aux tests (pas besoin de base de données)
    return {"status": "ok"}


@app.get("/db-check")
def db_check():
    # Vérifie que le backend arrive à parler à PostgreSQL
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"database": "connected"}