from tkinter import *
from tkinter import filedialog, messagebox
from configuration import Config

def save(i, protocol, path, window):
    if protocol == "py":
        try:
            if path.split()[len(path.split())] == "py":
                with open(path, "r+") as file:
                    code = file.readlines()
                    Config.set_btn(i=i, path=code, protocol=protocol)
                    messagebox.showinfo(title="Stream Deck | Edit", message="You must relaunch the app to refresh the button.")
            else:
                messagebox.showerror(title="Stream Deck | Error", message="The path you entered is not a python file.")
        except:
            messagebox.showerror(title="Stream Deck | Error", message="The path you entered is not valid.")
    else:
        Config.set_btn(i=i, path=path, protocol=protocol)
        window.destroy()

def run(protocol, text):

    config = Config()

    edit_window = Tk()
    edit_window.title(f"Stream Deck | Edit | {protocol}")
    edit_window.iconbitmap("assets/icon.ico")
    edit_window.config(bg=config.info["graphic"]["first"])
    edit_window.minsize(300, 130)
    edit_window.maxsize(300, 130)

    button_frame = Frame(edit_window, bg=config.info["graphic"]['first'])
    button_frame.pack()
    Label(button_frame, text=f"Button:", font=("Courrier", 15, "underline"), bg=config.info["graphic"]["first"], fg=config.info["graphic"]["second"]).pack(side=LEFT)
    choice = Spinbox(button_frame, from_=1, to=8, font=("Courrier", 15), bg=config.info["graphic"]["first"], fg=config.info["graphic"]["second"])
    choice.pack(side=RIGHT)

    path_frame = Frame(edit_window, bg=config.info["graphic"]["first"])
    path_frame.pack(fill=X, expand=YES)
    Label(path_frame, text=f"{text}:", font=("Courrier", 15, "underline"), bg=config.info["graphic"]["first"], fg=config.info["graphic"]["second"]).pack(side=LEFT)
    entry = Entry(path_frame, font=("Courrier", 15), bg=config.info["graphic"]["first"], fg=config.info["graphic"]["second"])
    entry.pack(fill=X, side=RIGHT)

    Button(edit_window, text="Save", bg=config.info["graphic"]["first"], fg=config.info["graphic"]["second"], font=("Courrier", 15, "bold"), command=lambda: [save(i=choice.get(), protocol=protocol, path=entry.get(), window=edit_window)]).pack(fill=X, padx=5, pady=5)

    if protocol == "py":
        menu_edit = Menu(menu, tearoff=0)

        menu.add_command(label="Exit", command=lambda: [edit_window.destroy()])
        menu.add_command(label="Help", command=lambda: [messagebox.showinfo(title="Stream Deck | Help", message="Name: Stream Deck\nBy Overdjoker048\nUpdate: Bêta 1.0\nSource: https://github.com/Overdjoker048/Stream-Deck")])

        window.mainloop()

    edit_window.mainloop()