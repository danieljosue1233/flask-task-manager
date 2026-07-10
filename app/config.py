import os

DB_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database.db")


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
