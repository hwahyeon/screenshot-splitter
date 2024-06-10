translations = {
    "English": {
        "settings": "Settings",
        "folder": "Change save folder",
        "language": "Language",
        "exit": "Exit",
        "help": "Help",
        "about": "About",
        "close": "Close",
        "left": "Left Monitor (L)",
        "right": "Right Monitor (R)",
        "take": "Take Screenshots (Alt+Z)",
        "open": "Open the folder (Alt+O)",
        "created": "Created by",
        "success": "Screenshots Saved!"
    },
    "한국어": {
        "settings": "!Settings",
        "folder": "Change save folder",
        "language": "Language",
        "exit": "Exit",
        "help": "Help",
        "about": "About",
        "close": "닫기",
        "left": "Left Monitor (L)",
        "right": "Right Monitor (R)",
        "take": "Take Screenshots (Alt+Z)",
        "open": "Open the folder (Alt+O)",
        "created": "Created by",
        "success": "Screenshots Saved!"
    },
    "Ελληνικά": {
        "settings": "!Settings",
        "folder": "Change save folder",
        "language": "Language",
        "exit": "Exit",
        "help": "Help",
        "about": "About",
        "close": "Close",
        "left": "Left Monitor (L)",
        "right": "Right Monitor (R)",
        "take": "Take Screenshots (Alt+Z)",
        "open": "Open the folder (Alt+O)",
        "created": "Created by",
        "success": "Screenshots Saved!"
    }
}

def get_text(language, text_key):
    print(language, text_key)
    return translations.get(language, {}).get(text_key, text_key)
