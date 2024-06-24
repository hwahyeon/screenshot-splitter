import tkinter as tk
from meun import creat_menu
from event import check_left_monitor, check_right_monitor, take_screenshots, open_folder, update_ui_texts
from tkinter import IntVar, Frame

def create_main_window(current_language, save_folder):
    # GUI setting
    root = tk.Tk()
    root.title("Screenshot Splitter")
    root.geometry("630x340")

    creat_menu(root)

    # Values for Checkbox
    left_monitor = IntVar()
    right_monitor = IntVar()

    # Checkbox
    left_monitor_check = tk.Checkbutton(root, text="Left Monitor (L)", variable=left_monitor)
    left_monitor_check.pack()
    right_monitor_check = tk.Checkbutton(root, text="Right Monitor (R)", variable=right_monitor)
    right_monitor_check.pack()

    # Binding for Shortcuts
    root.bind('<Alt-l>', lambda event: check_left_monitor(left_monitor))
    root.bind('<Alt-r>', lambda event: check_right_monitor(right_monitor))
    root.bind('<Alt-z>', lambda event: take_screenshots(root, preview_frame, left_monitor, right_monitor, save_folder, label, current_language))
    root.bind('<Alt-o>', lambda event: open_folder(save_folder))

    # Button (Take Screenshots)
    button1 = tk.Button(root, text="Take Screenshots (Alt+Z)",
                        command=lambda: take_screenshots(root, preview_frame, left_monitor, right_monitor, save_folder, label, current_language))
    button1.pack(pady=5)

    # Button (Open the folder)
    button2 = tk.Button(root, text="Open the folder (Alt+O)", command=lambda: open_folder(save_folder))
    button2.pack(pady=5)

    # Frame
    label_frame = tk.Frame(root)
    label_frame.pack(side=tk.BOTTOM)

    preview_frame = Frame(root)
    preview_frame.pack(pady=20)

    # Saved msg
    label = tk.Label(root, text="")
    label.pack(pady=10)

    # UI text update
    update_ui_texts(button1, button2, left_monitor_check, right_monitor_check, current_language)

    return root