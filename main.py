import tkinter as tk
from tkinter import IntVar
import mss
import os
import datetime
from PIL import Image
import time
import webbrowser
import platform

URL = "https://github.com/hwahyeon/py-screenshot-splitter"

def open_webpage(event=None):
    webbrowser.open(URL)

def check_left_monitor(event=None):
    left_monitor.set(not left_monitor.get())

def check_right_monitor(event=None):
    right_monitor.set(not right_monitor.get())

def take_screenshots(event=None):
    root.withdraw()
    time.sleep(0.5)

    with mss.mss() as sct:
        monitors = sct.monitors[1:]  # 첫 번째 항목(전체 화면)은 제외

        for monitor_number, monitor in enumerate(monitors, start=1):
            if (monitor_number == 1 and left_monitor.get()) or (monitor_number == 2 and right_monitor.get()):
                shot = sct.grab(monitor)
                img = Image.frombytes('RGB', (shot.width, shot.height), shot.rgb)
                filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_Monitor_{monitor_number}.png"
                img.save(os.path.join('screenshots', filename))

    root.deiconify()
    label.config(text="Screenshots Saved!")

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
root.title("Screenshot App")
root.geometry("200x180")

if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

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

button1 = tk.Button(root, text="Take Screenshots (Alt+Z)", command=take_screenshots)
button1.pack(pady=5)

button2 = tk.Button(root, text="Open the folder (Alt+O)", command=open_folder)
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

# Saved msg
label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()
