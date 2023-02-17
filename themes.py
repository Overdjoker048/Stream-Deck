from os import path
from json import dump, load
from tkinter import messagebox

def get_theme():
    if path.exists("assets/config.json"):
        try:
            with open("assets/config.json", "r+") as file:
                content = load(fp=file)
        except:
            content = {
                "first": "white",
                "second": "#252525",
                "texture": "assets/white_key.png"
            }
    else:
        content = {
            "first": "white",
            "second": "#252525",
            "texture": "assets/white_key.png"
        }

    return content


def set(first, second, texture):
    info = {
        "first": first,
        "second": second,
        "texture": texture
    }
    with open("assets/config.json", "w+") as file:
        dump(info, file, indent=2)
    messagebox.showinfo(title="Stream Deck | Themes", message="To apply the themes you must restart\nthe stream deck.")