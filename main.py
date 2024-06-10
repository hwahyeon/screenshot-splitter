import tkinter as tk
from tkinter import IntVar, Label, Frame, messagebox, filedialog
import mss
import os
import datetime
from PIL import Image, ImageTk
import time
import webbrowser
import platform
from langs import get_text

current_language = "English"
URL = "https://github.com/hwahyeon/py-screenshot-splitter"

def set_app_language(lang):
    global current_language
    current_language = lang

def open_webpage(event=None):
    webbrowser.open(URL)

def check_left_monitor(event=None):
    left_monitor.set(not left_monitor.get())

def check_right_monitor(event=None):
    right_monitor.set(not right_monitor.get())

def take_screenshots(event=None):
    root.withdraw()
    time.sleep(0.5)

    screenshots = []

    with mss.mss() as sct:
        monitors = sct.monitors[1:]  # sct.monitors[0]: Full screen

        for monitor_number, monitor in enumerate(monitors, start=1):
            if (monitor_number == 1 and left_monitor.get()) or (monitor_number == 2 and right_monitor.get()):
                shot = sct.grab(monitor)
                img = Image.frombytes('RGB', (shot.width, shot.height), shot.rgb)
                screenshots.append((img, monitor_number))

                filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_Monitor_{monitor_number}.png"
                img.save(os.path.join('screenshots', filename))

    root.deiconify()
    label.config(text=get_text(current_language, "success"))
    root.after(2000, clear_label)

    # Reset preview frame
    for widget in preview_frame.winfo_children():
        widget.destroy()

    for img, monitor_number in screenshots:
        show_preview(img)

    root.deiconify()
    label.config(text=get_text(current_language, "success"))
    root.after(2000, clear_label)

def clear_label():
    label.config(text="")

def show_preview(img):
    img.thumbnail((300, 300))  # preview size

    img_tk = ImageTk.PhotoImage(img)
    preview_label = Label(preview_frame, image=img_tk)
    preview_label.image = img_tk
    preview_label.pack(side=tk.LEFT, padx=10)

def open_folder(event=None):
    folder_path = os.getcwd() + "\\screenshots"

    if platform.system() == "Windows":
        os.startfile(folder_path)
    elif platform.system() == "Darwin":  # macOS
        os.system(f"open {folder_path}")
    else:  # Linux
        os.system(f"xdg-open {folder_path}")



# GUI setting
root = tk.Tk()
root.title("Screenshot Splitter")
root.geometry("630x340")

# Folder
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

def change_folder_location():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        tk.messagebox.showinfo("Folder Selected", f"Selected folder: {folder_selected}")


def change_language():
    selected_language = lang_var.get()
    set_app_language(selected_language)
    print(selected_language)
    print(current_language)
    tk.messagebox.showinfo("Language Changed", f"Selected language: {selected_language}")


def on_exit():
    root.quit()


def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_window.geometry("190x130")

    about_label = tk.Label(about_window, text=("Screenshot Splitter\n"
                                               "Created by hwahyeon\n"), justify="center")
    about_label.pack(pady=20)

    close_button = tk.Button(about_window, text=get_text(current_language, "close"), command=about_window.destroy)
    close_button.pack(pady=10)


# Menu bar
menu_bar = tk.Menu(root)

# 'Settings' Menu
settings_menu = tk.Menu(menu_bar, tearoff=0)
settings_menu.add_command(label=get_text(current_language, "folder"), command=change_folder_location)

# Language sub menu and check box
lang_var = tk.StringVar(value="English")
language_menu = tk.Menu(settings_menu, tearoff=0)
languages = ["English", "한국어", "Ελληνικά"]

for lang in languages:
    language_menu.add_radiobutton(label=lang, variable=lang_var, value=lang, command=change_language)

settings_menu.add_cascade(label=get_text(current_language, "language"), menu=language_menu)
settings_menu.add_separator()
settings_menu.add_command(label=get_text(current_language, "exit"), command=on_exit)

# Add 'Settings' menu
menu_bar.add_cascade(label=get_text(current_language, "settings"), menu=settings_menu)

# 'Help' menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label=get_text(current_language, "about"), command=show_about)
menu_bar.add_cascade(label=get_text(current_language, "help"), menu=help_menu)

# Add menu bar
root.config(menu=menu_bar)

# Values for Checkbox
left_monitor = IntVar()
right_monitor = IntVar()

# Checkboxs
left_monitor_check = tk.Checkbutton(root, text=get_text(current_language, "left"), variable=left_monitor)
left_monitor_check.pack()
right_monitor_check = tk.Checkbutton(root, text=get_text(current_language, "right"), variable=right_monitor)
right_monitor_check.pack()

# Binding for Shortcuts
root.bind('<Alt-l>', check_left_monitor)
root.bind('<Alt-r>', check_right_monitor)
root.bind('<Alt-z>', take_screenshots)
root.bind('<Alt-o>', open_folder)

# Button (Take Screenshots)
button1 = tk.Button(root, text=get_text(current_language, "take"), command=take_screenshots)
button1.pack(pady=5)

# Button (Open the folder)
button2 = tk.Button(root, text=get_text(current_language, "open"), command=open_folder)
button2.pack(pady=5)

# Frame for 2 labels ("Created by" + "Name")
label_frame = tk.Frame(root)
label_frame.pack(side=tk.BOTTOM)

# "Created by"
created_label = tk.Label(label_frame, text="Created by")
created_label.pack(side=tk.LEFT)

# "Name"
name_label = tk.Label(label_frame, text="hwahyeon", fg="blue", cursor="hand2")
name_label.pack(side=tk.LEFT)
name_label.bind("<Button-1>", open_webpage)

# Created and positioned preview frames
global preview_frame
preview_frame = Frame(root)
preview_frame.pack(pady=20)

# Saved msg
label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()
