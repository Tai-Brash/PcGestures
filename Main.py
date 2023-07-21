import base64
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the environment variables using os.getenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

# Print the values of CLIENT_ID and CLIENT_SECRET
print("CLIENT_ID: " + str(client_id))
print("CLIENT_SECRET: " + str(client_secret))


def get_token():
    auth_string = client_id + ":" + client_secret
    authbytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_base64), "utf-8")