from database import init_db
from settings import init_app_settings, get_save_folder, get_current_language
from window import create_main_window
from menu import update_ui_menus


class MainApp:
    def __init__(self):
        self.init_app_settings()
        self.current_language = get_current_language()
        self.save_folder = get_save_folder()

        init_db()
        self.root, self.language, self.menu_bar, self.help_menu, self.settings_menu = create_main_window(
            self.current_language, self.save_folder, self.set_language_value)

    @staticmethod
    def init_app_settings():
        init_app_settings()

    @staticmethod
    def set_language_value(self, value, language):
        language.set(value)

    def run(self):
        self.root.mainloop()

    def refresh_ui(self):
        update_ui_menus(self.current_language, self.menu_bar, self.help_menu, self.settings_menu)


if __name__ == "__main__":
    app = MainApp()
    app.run()
