import os
from database import init_db, load_setting, save_setting


def init_app_settings():
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    init_db()
    if not load_setting('current_language'):
        save_setting('current_language', 'English')
    if not load_setting('save_folder'):
        save_setting('save_folder', os.path.join(os.getcwd(), 'screenshots'))


def get_save_folder():
    return load_setting('save_folder', os.path.join(os.getcwd(), 'screenshots'))


def get_current_language():
    return load_setting('current_language', 'English')
