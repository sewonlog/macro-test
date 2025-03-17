import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
db_password = os.getenv("DB_PASSWORD")

print(api_key, db_password)
