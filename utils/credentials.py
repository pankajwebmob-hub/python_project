import json
import os

def get_credentials():
    # Get path to credentials.json
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "credentials.json")

    # Read the JSON file
    with open(file_path, "r") as file:
        credentials = json.load(file)

    # Ensure both keys exist
    if "username" not in credentials or "password" not in credentials:
        raise ValueError("Missing 'username' or 'password' in credentials.json")

    return credentials
