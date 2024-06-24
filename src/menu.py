import tkinter as tk
from tkinter import messagebox
from about import show_about
from database import save_setting
from langs import get_text
from folder import change_folder_location
from settings import init_app_settings, get_save_folder, get_current_language


def update_ui_lang_texts(buttons, language):
    keys = ["take", "open", "left", "right"]
    for button, key in zip(buttons, keys):
        button.config(text=get_text(language, key))


def set_app_language(current_language, menu_bar, help_menu, settings_menu):
    save_setting('current_language', current_language)
    update_ui_menus(current_language, menu_bar, help_menu, settings_menu)


def update_ui_menus(current_language, menu_bar, help_menu, settings_menu):
    # Menu
    menu_bar.entryconfig(1, label=get_text(current_language, "settings"))
    menu_bar.entryconfig(2, label=get_text(current_language, "help"))
    help_menu.entryconfig(0, label=get_text(current_language, "about"))
    settings_menu.entryconfig(0, label=get_text(current_language, "folder"))
    settings_menu.entryconfig(1, label=get_text(current_language, "settings"))
    settings_menu.entryconfig(3, label=get_text(current_language, "exit"))


def change_language(lang_var, menu_bar, help_menu, settings_menu, toggle_language_callback):
    selected_language = lang_var.get()
    current_language = selected_language
    set_app_language(selected_language, menu_bar, help_menu, settings_menu)
    messagebox.showinfo(get_text(current_language, "lang_change_title"),
                        (get_text(current_language, "lang_change_cont") + selected_language))
    toggle_language_callback(selected_language)


def create_menu(root, current_language, save_folder, toggle_language_callback):
    # Menu bar
    menu_bar = tk.Menu(root)

    # 'Settings' Menu
    settings_menu = tk.Menu(menu_bar, tearoff=0)
    settings_menu.add_command(label=get_text(current_language, "folder"),
                              command=lambda: change_folder_location(save_folder, save_setting, current_language))

    # Language sub menu and check box
    lang_var = tk.StringVar(value=get_current_language())
    language_menu = tk.Menu(settings_menu, tearoff=0)
    languages = ["English", "한국어", "Ελληνικά"]

    for lang in languages:
        language_menu.add_radiobutton(label=lang, variable=lang_var, value=lang,
                                      command=lambda: change_language(lang_var, menu_bar, help_menu, settings_menu,
                                                                      toggle_language_callback))

    settings_menu.add_cascade(label=get_text(current_language, "language"), menu=language_menu)
    settings_menu.add_separator()
    settings_menu.add_command(label=get_text(current_language, "exit"), command=lambda: on_exit(root))

    # Add 'Settings' menu
    menu_bar.add_cascade(label=get_text(current_language, "settings"), menu=settings_menu)

    # 'Help' menu
    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label=get_text(current_language, "about"), command=lambda: show_about(root, current_language))
    menu_bar.add_cascade(label=get_text(current_language, "help"), menu=help_menu)

    # Add menu bar
    root.config(menu=menu_bar)

    return menu_bar, help_menu, settings_menu


def on_exit(root):
    root.quit()
