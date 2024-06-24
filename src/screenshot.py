import datetime
from PIL import Image, ImageTk
import time
import mss
from tkinter import Label, LEFT
import os
from langs import get_text
from settings import get_current_language

def take_screenshots(root, preview_frame, left_monitor, right_monitor, save_folder, label,
                     event=None):
    current_language = get_current_language()
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

    # Reset preview frame
    for widget in preview_frame.winfo_children():
        widget.destroy()

    for img, monitor_number in screenshots:
        show_preview(preview_frame, img)

    root.deiconify()
    label.config(text=get_text(current_language, "success"))
    root.after(2000, lambda: clear_label(label))


def clear_label(label):
    label.config(text="")


def show_preview(preview_frame, img):
    img.thumbnail((300, 300))  # preview size

    img_tk = ImageTk.PhotoImage(img)
    preview_label = Label(preview_frame, image=img_tk)
    preview_label.image = img_tk
    preview_label.pack(side=LEFT, padx=10)
