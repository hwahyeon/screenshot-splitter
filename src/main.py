from database import init_db
from settings import init_app_settings, get_save_folder, get_current_language
from window import create_main_window


class MainApp:
    def __init__(self):
        self.init_app_settings()
        self.current_language = get_current_language()
        self.save_folder = get_save_folder()

        init_db()
        self.root = create_main_window(self.current_language, self.save_folder)

    @staticmethod
    def init_app_settings():
        init_app_settings()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MainApp()
    app.run()
