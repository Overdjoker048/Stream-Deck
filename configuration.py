from os import path
from json import dump, load
from tkinter import messagebox

default = {
        "graphic": {
            "first": "white",
            "second": "#252525",
            "texture": path.join("assets", "white_key.png")
        },
        "button1": {
            "protocol": "",
            "path": ""
        },
        "button2": {
            "protocol": "",
            "path": ""
        },
        "button3": {
            "protocol": "",
            "path": ""
        },
        "button4": {
            "protocol": "",
            "path": ""
        },
        "button5": {
            "protocol": "",
            "path": ""
        },
        "button6": {
            "protocol": "",
            "path": ""
        },
        "button7": {
            "protocol": "",
            "path": ""
        },
        "button8": {
            "protocol": "",
            "path": ""
        }
    }

if not path.exists(path.join("assets", "config.json")):
    with open(path.join("assets", "config.json"), "w+") as file:
        dump(default, file, indent=2)

class Config:
    def __init__(self):
        try:
            with open(path.join("assets", "config.json"), "r+") as file:
                self.info = load(fp=file)
        except:
            if not path.exists(path.join("assets", "config.json")):
                with open(path.join("assets", "config.json"), "w+") as file:
                    dump(default, file, indent=2)

    def set_btn(self, i, protocol, path):
        self.info[f"button{i}"]["protocol"] = protocol
        self.info[f"button{i}"]["path"] = path
        self.update()

    def set_themes(self, first, second, texture):
        self.info["graphic"]["first"] = first
        self.info["graphic"]["second"] = second
        self.info["graphic"]["texture"] = texture
        self.update()

    def update(self):
        with open(path.join("assets", "config.json"), "w") as file:
            dump(self.info, file, indent=2)
        messagebox.showinfo(title="Stream Deck | Themes", message="To apply the themes you must restart\nthe stream deck.")