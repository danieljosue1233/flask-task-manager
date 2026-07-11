import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Config:
    uri = os.getenv("DATABASE_URL", f"sqlite:///{os.path.join(basedir, 'database.db')}")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "clave-segura-por-defecto")


class TestConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "clave-segura-por-defecto")
    TESTING = True
