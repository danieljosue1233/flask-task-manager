import os

DB_FILE = os.path.join(os.path.dirname(__file__), "database.db")


class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_FILE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "clave-secreta-cambiar-en-produccion"
