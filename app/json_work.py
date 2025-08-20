import json


def get_profiles() -> list[dict]:
    with open("profiles.json", "r", encoding="utf-8") as file:
        return json.load(file)
    