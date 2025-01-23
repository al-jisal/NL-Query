import os 
import openai
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY")
    openai.api_key = OPENAI_API_KEY
