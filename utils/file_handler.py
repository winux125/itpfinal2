import json
import os

def load_json(filepath: str) -> list:
    # read the json file
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading {filepath}: {e}")
        return []

def save_json(filepath: str, data: list):
    # save the list to json
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving to {filepath}: {e}")
