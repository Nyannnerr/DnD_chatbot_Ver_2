import os
from dotenv import load_dotenv

# Load các biến môi trường từ file .env
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def validate_config():
    if not DISCORD_TOKEN or not GEMINI_API_KEY:
        raise ValueError("Missing DISCORD_TOKEN or GEMINI_API_KEY in .env file")
    return True
