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
import sqlite3

URL = "https://github.com/hwahyeon/py-screenshot-splitter"

# SQLite
def init_db():
    conn = sqlite3.connect('settings.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    ''')
    if not load_setting('current_language'):
        c.execute('INSERT INTO settings (key, value) VALUES (?, ?)', ('current_language', 'English'))
    if not load_setting('save_folder'):
        c.execute('INSERT INTO settings (key, value) VALUES (?, ?)',
                  ('save_folder', os.path.join(os.getcwd(), 'screenshots')))
    conn.commit()
    conn.close()

def save_setting(key, value):
    conn = sqlite3.connect('settings.db')
    c = conn.cursor()
    c.execute('''
        INSERT OR REPLACE INTO settings (key, value)
        VALUES (?, ?)
    ''', (key, value))
    conn.commit()
    conn.close()

def load_setting(key, default=None):
    conn = sqlite3.connect('settings.db')
    c = conn.cursor()
    c.execute('''
        SELECT value FROM settings WHERE key = ?
    ''', (key,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else default

init_db()
current_language = load_setting('current_language', 'English')
save_folder = load_setting('save_folder', os.path.join(os.getcwd(), 'screenshots'))

def set_app_language(lang):
    global current_language
    current_language = lang
    save_setting('current_language', current_language)
    update_ui_texts()

def update_ui_texts():
    # Menu
    menu_bar.entryconfig(1, label=get_text(current_language, "settings"))
    menu_bar.entryconfig(2, label=get_text(current_language, "help"))
    help_menu.entryconfig(0, label=get_text(current_language, "about"))
    settings_menu.entryconfig(0, label=get_text(current_language, "folder"))
    settings_menu.entryconfig(1, label=get_text(current_language, "settings"))
    settings_menu.entryconfig(3, label=get_text(current_language, "exit"))
    # label
    button1.config(text=get_text(current_language, "take"))
    button2.config(text=get_text(current_language, "open"))
    left_monitor_check.config(text=get_text(current_language, "left"))
    right_monitor_check.config(text=get_text(current_language, "right"))

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
                img.save(os.path.join(save_folder, filename))

    root.deiconify()
    label.config(text="Screenshots Saved!")
    root.after(2000, clear_label)

    # Reset preview frame
    for widget in preview_frame.winfo_children():
        widget.destroy()

    for img, monitor_number in screenshots:
        show_preview(img)

    root.deiconify()
    label.config(text="Screenshots Saved!")
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
    if platform.system() == "Windows":
        os.startfile(save_folder)
    elif platform.system() == "Darwin":  # macOS
        os.system(f"open {save_folder}")
    else:  # Linux
        os.system(f"xdg-open {save_folder}")

def change_folder_location():
    global save_folder

    folder_selected = filedialog.askdirectory()
    if folder_selected:
        save_folder = folder_selected
        save_setting('save_folder', save_folder)
        tk.messagebox.showinfo("Folder Selected", f"Selected folder: {save_folder}")

def change_language():
    selected_language = lang_var.get()
    set_app_language(selected_language)
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

    # "Created by"
    created_label = tk.Label(about_window, text="Created by")
    created_label.pack(side=tk.LEFT)

    # "Name"
    name_label = tk.Label(about_window, text="hwahyeon", fg="blue", cursor="hand2")
    name_label.pack(side=tk.LEFT)
    name_label.bind("<Button-1>", open_webpage)

    close_button = tk.Button(about_window, text=get_text(current_language, "close"), command=about_window.destroy)
    close_button.pack(pady=10)

# GUI setting
root = tk.Tk()
root.title("Screenshot Splitter")
root.geometry("630x340")

# Folder
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Menu bar
menu_bar = tk.Menu(root)

# 'Settings' Menu
settings_menu = tk.Menu(menu_bar, tearoff=0)
settings_menu.add_command(label="Change save folder", command=change_folder_location)

# Language sub menu and check box
lang_var = tk.StringVar(value="English")
language_menu = tk.Menu(settings_menu, tearoff=0)
languages = ["English", "한국어", "Ελληνικά"]

for lang in languages:
    language_menu.add_radiobutton(label=lang, variable=lang_var, value=lang, command=change_language)

settings_menu.add_cascade(label="Language", menu=language_menu)
settings_menu.add_separator()
settings_menu.add_command(label="Exit", command=on_exit)

# Add 'Settings' menu
menu_bar.add_cascade(label="Settings", menu=settings_menu)

# 'Help' menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Add menu bar
root.config(menu=menu_bar)

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
button1 = tk.Button(root, text="Take Screenshots (Alt+Z)", command=take_screenshots)
button1.pack(pady=5)

# Button (Open the folder)
button2 = tk.Button(root, text="Open the folder (Alt+O)", command=open_folder)
button2.pack(pady=5)

# Frame for 2 labels ("Created by" + "Name")
label_frame = tk.Frame(root)
label_frame.pack(side=tk.BOTTOM)

# Created and positioned preview frames
global preview_frame
preview_frame = Frame(root)
preview_frame.pack(pady=20)

# Saved msg
label = tk.Label(root, text="")
label.pack(pady=10)

# UI text update
update_ui_texts()

root.mainloop()
