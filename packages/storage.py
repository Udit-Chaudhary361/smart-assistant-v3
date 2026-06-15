import json
import os

def load_data():
    if os.path.exists("assistant_data.json"):
        with open("assistant_data.json" , "r") as f:
            return json.load(f)
    return {
            "name": "",
            "notes": [],
            "tasks": []
                        }

def save_data(data):
    with open("assistant_data.json" , "w") as f:
        json.dump(data , f ,indent=4)