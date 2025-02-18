import os

class Config:
    OPENAI_API_KEY = os.getenv("sk-ijklmnop5678efghijklmnop5678efghijklmnop")
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False