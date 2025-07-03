import sqlite3
import os
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(__file__)

DB_PATH = os.path.join(BASE_DIR, 'settings.db')


def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    ''')
    conn.commit()

    if not load_setting('current_language'):
        c.execute('INSERT INTO settings (key, value) VALUES (?, ?)', ('current_language', 'English'))
    if not load_setting('save_folder'):
        c.execute('INSERT INTO settings (key, value) VALUES (?, ?)',
                  ('save_folder', os.path.join(os.getcwd(), 'screenshots')))

    conn.close()


def save_setting(key, value):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT OR REPLACE INTO settings (key, value)
        VALUES (?, ?)
    ''', (key, value))
    conn.commit()
    conn.close()


def load_setting(key, default=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        SELECT value FROM settings WHERE key = ?
    ''', (key,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else default
