import os
from dotenv import load_dotenv

# Muat variabel lingkungan dari file .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')  # Ganti dengan fallback jika tidak ada di .env
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600))  # Fallback jika tidak ada
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES', 86400))  # Fallback jika tidak ada
