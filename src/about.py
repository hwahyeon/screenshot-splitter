import tkinter as tk
import webbrowser
from langs import get_text

URL = "https://github.com/hwahyeon/py-screenshot-splitter"


def open_webpage(event=None):
    webbrowser.open(URL)


def show_about(root, current_language):
    about_window = tk.Toplevel(root)
    about_window.title(get_text(current_language, "about"))
    about_window.geometry("190x130")

    about_label = tk.Label(about_window, text=("Screenshot Splitter\n"
                                               "v 2.0.0\n"), justify="center")
    about_label.pack(pady=10)

    # "Created by"
    created_label = tk.Label(about_window, text=get_text(current_language, "create"))
    created_label.pack(side=tk.LEFT)

    # "Name"
    name_label = tk.Label(about_window, text="hwahyeon", fg="blue", cursor="hand2")
    name_label.pack(side=tk.LEFT)
    name_label.bind("<Button-1>", open_webpage)
