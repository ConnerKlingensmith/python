import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Acces environemtn variables
username = os.getenv("DEVICE_USERNAME")
password = os.getenv("DEVICE_PASSWORD")
api_key = os.getenv("API_KEY")

print(f"Connecting as: {username}")

# Provide default value if not found
debug_mode = os.getenv("DEBUG_MODE", "False")
