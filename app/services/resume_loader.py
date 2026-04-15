import json

def load_resume():
    with open("app/data/resume.json", "r") as f:
        return json.load(f)