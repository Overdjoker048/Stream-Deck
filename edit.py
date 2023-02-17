from tkinter import *
import themes

def run(protocol, text):

    color = themes.get_theme()

    edit_window = Tk()
    edit_window.title("Stream Deck | Edit")
    edit_window.iconbitmap("assets/icon.ico")
    edit_window.config(bg=color["first"])
    edit_window.minsize(300, 130)
    edit_window.maxsize(300, 130)

    button_frame = Frame(edit_window, bg=color['first'])
    button_frame.pack()
    Label(button_frame, text=f"Button:", font=("Courrier", 15, "underline"), bg=color["first"], fg=color["second"]).pack(side=LEFT)
    choice = Spinbox(button_frame, from_=1, to=8, font=("Courrier", 15), bg=color["first"], fg=color["second"])
    choice.pack(side=RIGHT)

    path_frame = Frame(edit_window, bg=color["first"])
    path_frame.pack(fill=X, expand=YES)
    Label(path_frame, text=f"{text}:", font=("Courrier", 15, "underline"), bg=color["first"], fg=color["second"]).pack(side=LEFT)
    entry_path = Entry(path_frame, font=("Courrier", 15), bg=color["second"], fg=color["first"], borderwidth=0)
    entry_path.pack(fill=X, side=RIGHT)

    Button(edit_window, text="Save", bg=color["second"], fg=color["first"], font=("Courrier", 15, "bold")).pack(fill=X, padx=5, pady=10)

    edit_window.mainloop()

def py():
    color = themes.get_theme()

    edit_window = Tk()
    edit_window.title("Stream Deck | Edit")
    edit_window.iconbitmap("assets/icon.ico")
    edit_window.config(bg=color["first"])
    edit_window.minsize(300, 250)
    edit_window.maxsize(300, 250)

    button_frame = Frame(edit_window, bg=color['first'])
    button_frame.pack(pady=5)
    Label(button_frame, text=f"Button:", font=("Courrier", 15, "underline"), bg=color["first"], fg=color["second"]).pack(side=LEFT)
    choice = Spinbox(button_frame, from_=1, to=8, font=("Courrier", 15), bg=color["first"], fg=color["second"])
    choice.pack(side=RIGHT)

    text = Text(edit_window, font=("Courrier"), bg=color["first"], fg=color["second"], height=7.5)
    text.pack(pady=5, padx=5)

    Button(edit_window, text="Save", bg=color["second"], fg=color["first"], font=("Courrier", 15, "bold")).pack(fill=X, padx=5, pady=10)

    edit_window.mainloop()