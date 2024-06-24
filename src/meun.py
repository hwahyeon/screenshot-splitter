import tkinter as tk
from about import show_about
from database import save_setting, load_setting
from langs import get_text
from folder import change_folder_location
import os

save_folder = load_setting('save_folder', os.path.join(os.getcwd(), 'screenshots'))
current_language = load_setting('current_language', 'English')


def set_app_language(current_language):
    save_setting('current_language', current_language)
    update_ui_menus(menu_bar, help_menu, settings_menu)


def update_ui_menus(menu_bar, help_menu, settings_menu):
    # Menu
    menu_bar.entryconfig(1, label=get_text(current_language, "settings"))
    menu_bar.entryconfig(2, label=get_text(current_language, "help"))
    help_menu.entryconfig(0, label=get_text(current_language, "about"))
    settings_menu.entryconfig(0, label=get_text(current_language, "folder"))
    settings_menu.entryconfig(1, label=get_text(current_language, "settings"))
    settings_menu.entryconfig(3, label=get_text(current_language, "exit"))


def change_language(lang_var):
    selected_language = lang_var.get()
    set_app_language(selected_language)
    tk.messagebox.showinfo(get_text(current_language, "lang_change_title"),
                           (get_text(current_language, "lang_change_cont") + selected_language))


def creat_menu(root):
    # Menu bar
    menu_bar = tk.Menu(root)

    # 'Settings' Menu
    settings_menu = tk.Menu(menu_bar, tearoff=0)
    settings_menu.add_command(label="Change save folder",
                              command=lambda: change_folder_location(save_folder, save_setting, current_language))

    # Language sub menu and check box
    lang_var = tk.StringVar(value="English")
    language_menu = tk.Menu(settings_menu, tearoff=0)
    languages = ["English", "한국어", "Ελληνικά"]

    for lang in languages:
        language_menu.add_radiobutton(label=lang, variable=lang_var, value=lang, command=lambda: change_language(lang_var))

    settings_menu.add_cascade(label="Language", menu=language_menu)
    settings_menu.add_separator()
    settings_menu.add_command(label="Exit", command=lambda: on_exit(root))

    # Add 'Settings' menu
    menu_bar.add_cascade(label="Settings", menu=settings_menu)

    # 'Help' menu
    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About", command=lambda: show_about(root, current_language))
    menu_bar.add_cascade(label="Help", menu=help_menu)

    # Add menu bar
    root.config(menu=menu_bar)


def on_exit(root):
    root.quit()
