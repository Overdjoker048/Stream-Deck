from tkinter import *
from tkinter import messagebox
from webbrowser import open
from os import system
import themes, edit

def run():

    color = themes.get_theme()

    window = Tk()
    window.title("Stream Deck")
    window.overrideredirect(True)
    window.wm_attributes("-topmost", True)
    menu = Menu(window)
    window.iconbitmap("assets/icon.ico")
    window.config(bg=color['first'], menu=menu)
    frames = [Frame(window, bg=color['first']), Frame(window, bg=color['first'])]
    frames[0].pack(fill=X, side=TOP)
    frames[1].pack(fill=X, side=TOP)
    texture = PhotoImage(file=color['texture'])
    for frame in frames:
        for i in range(4):
            Button(frame, image=texture, bg=color['first'], fg=color['first'], relief=FLAT, bd=0, highlightthickness=0, activebackground=color['first']).pack(pady=7.5, padx=7.5, side=LEFT)

    menu_themes = Menu(menu, tearoff=0)
    menu.add_cascade(label="Themes", menu=menu_themes)
    menu_themes.add_command(label="Dark", command=lambda: [themes.set("#353535", "white", "assets/black_key.png")])
    menu_themes.add_command(label="Light", command=lambda: [themes.set("white", "#252525", "assets/white_key.png")])

    menu_edit = Menu(menu, tearoff=0)
    menu.add_cascade(label="Edit", menu=menu_edit)
    menu_edit.add_command(label="Python", command=lambda: [edit.py()])
    menu_edit.add_command(label="Web", command=lambda: [edit.run("web", "URL")])
    menu_edit.add_command(label="Application", command=lambda: [edit.run("app", "Name")])

    menu.add_command(label="Exit", command=lambda: [window.destroy()])
    menu.add_command(label="Help", command=lambda: [messagebox.showinfo(title="Stream Deck | Help", message="Name: Stream Deck\nBy Overdjoker048\nUpdate: Bêta 1.0\nSource: https://github.com/Overdjoker048/Stream-Deck")])

    window.mainloop()