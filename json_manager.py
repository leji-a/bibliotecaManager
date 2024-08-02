import json
import os

def read_json():
    if not os.path.isfile("books_list.json"):
        with open("books_list.json", "w") as f:
            json.dump([], f, indent=4)
    with open("books_list.json", "r") as f:
        data = json.load(f)
    return data

def write_json(data):
    with open("books_list.json", "w") as f:
        json.dump(data, f, indent=4)
