import tkinter as tk
from tkinter import IntVar, Frame
from menu import create_menu, update_ui_lang_texts
from event import check_left_monitor, check_right_monitor, take_screenshots, open_folder
from langs import get_text


def create_main_window(current_language, save_folder, toggle_language_callback):
    # GUI setting
    root = tk.Tk()
    root.title("Screenshot Splitter")
    root.geometry("630x355")

    # menu_bar, help_menu, settings_menu = create_menu(root, current_language, save_folder)
    menu_bar, help_menu, settings_menu = create_menu(root, current_language, save_folder,
                                                     lambda value: toggle_language_callback(value, language))

    # Values for Checkbox
    left_monitor = IntVar()
    right_monitor = IntVar()

    # Checkbox
    left_monitor_check = tk.Checkbutton(root, text=get_text(current_language, "left"), variable=left_monitor)
    left_monitor_check.pack()
    right_monitor_check = tk.Checkbutton(root, text=get_text(current_language, "right"), variable=right_monitor)
    right_monitor_check.pack()

    # Binding for Shortcuts
    root.bind('<Alt-l>', lambda event: check_left_monitor(left_monitor))
    root.bind('<Alt-r>', lambda event: check_right_monitor(right_monitor))
    root.bind('<Alt-z>',
              lambda event: take_screenshots(root, preview_frame, left_monitor, right_monitor, save_folder, label
                                             ))
    root.bind('<Alt-o>', lambda event: open_folder(save_folder))

    # Button (Take Screenshots)
    button1 = tk.Button(root, text=get_text(current_language, "take"),
                        command=lambda: take_screenshots(root, preview_frame, left_monitor, right_monitor, save_folder,
                                                         label, current_language))
    button1.pack(pady=5)

    # Button (Open the folder)
    button2 = tk.Button(root, text=get_text(current_language, "open"), command=lambda: open_folder(save_folder))
    button2.pack(pady=5)

    # Preview Frame
    preview_frame = Frame(root)
    preview_frame.pack(pady=10)

    # Saved msg
    label = tk.Label(root, text="")
    label.pack(pady=5)

    # UI text update
    # update_ui_texts(button1, button2, left_monitor_check, right_monitor_check, current_language)

    # UI list
    ui_list = [button1, button2, left_monitor_check, right_monitor_check]

    # IntVar (trace for language)
    language = tk.StringVar(value="")

    def on_language_change(*args):
        # print(f"a changed to {language.get()}")
        update_ui_lang_texts(ui_list, language.get())

    language.trace_add("write", on_language_change)

    return root, language, menu_bar, help_menu, settings_menu


def update_ui_texts(button1, button2, left_monitor_check, right_monitor_check, current_language):
    button1.config(text=get_text(current_language, "take"))
    button2.config(text=get_text(current_language, "open"))
    left_monitor_check.config(text=get_text(current_language, "left"))
    right_monitor_check.config(text=get_text(current_language, "right"))
