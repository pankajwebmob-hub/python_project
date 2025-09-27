import os
import json
# 👇 This will return all users' credentials as a dict
def get_all_credentials():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "credentials.json")

    with open(file_path, "r") as file:
        return json.load(file)
