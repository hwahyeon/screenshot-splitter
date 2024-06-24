import tkinter as tk
from tkinter import IntVar, Frame, messagebox
import os
from langs import get_text
from database import init_db, save_setting, load_setting
from folder import open_folder, change_folder_location
from screenshot import take_screenshots
from meun import creat_menu

init_db()
current_language = load_setting('current_language', 'English')
save_folder = load_setting('save_folder', os.path.join(os.getcwd(), 'screenshots'))


def update_ui_texts():
    # label
    button1.config(text=get_text(current_language, "take"))
    button2.config(text=get_text(current_language, "open"))
    left_monitor_check.config(text=get_text(current_language, "left"))
    right_monitor_check.config(text=get_text(current_language, "right"))


def check_left_monitor(event=None):
    left_monitor.set(not left_monitor.get())


def check_right_monitor(event=None):
    right_monitor.set(not right_monitor.get())


# GUI setting
root = tk.Tk()
root.title("Screenshot Splitter")
root.geometry("630x340")

# Folder
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

creat_menu(root)

# Values for Checkbox
left_monitor = IntVar()
right_monitor = IntVar()

# Checkboxs
left_monitor_check = tk.Checkbutton(root, text="Left Monitor (L)", variable=left_monitor)
left_monitor_check.pack()
right_monitor_check = tk.Checkbutton(root, text="Right Monitor (R)", variable=right_monitor)
right_monitor_check.pack()

# Binding for Shortcuts
root.bind('<Alt-l>', check_left_monitor)
root.bind('<Alt-r>', check_right_monitor)
root.bind('<Alt-z>', take_screenshots)
root.bind('<Alt-o>', open_folder)

# Button (Take Screenshots)
button1 = tk.Button(root, text="Take Screenshots (Alt+Z)",
                    command=lambda: take_screenshots(root, preview_frame, left_monitor, right_monitor, save_folder,
                                                     label, current_language))
button1.pack(pady=5)

# Button (Open the folder)
button2 = tk.Button(root, text="Open the folder (Alt+O)", command=lambda: open_folder(save_folder))
button2.pack(pady=5)

# Frame for 2 labels ("Created by" + "Name")
label_frame = tk.Frame(root)
label_frame.pack(side=tk.BOTTOM)

# Created and positioned preview frames
preview_frame = Frame(root)
preview_frame.pack(pady=20)

# Saved msg
label = tk.Label(root, text="")
label.pack(pady=10)

# UI text update
update_ui_texts()

root.mainloop()
