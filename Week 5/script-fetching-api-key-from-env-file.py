from dotenv import load_dotenv
import os

load_dotenv()   # reads .env and sets environment variables

api_key = os.getenv("SMP_API_KEY")
print(api_key)