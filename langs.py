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
        "settings": "설정",
        "folder": "저장할 폴더 선택",
        "language": "언어",
        "exit": "나가기",
        "help": "도움",
        "about": "정보",
        "close": "닫기",
        "left": "왼쪽 모니터 (L)",
        "right": "오른쪽 모니터 (R)",
        "take": "스크린샷 찍기 (Alt+Z)",
        "open": "저장 폴더 열기 (Alt+O)",
        "created": "Created by",
        "success": "스크린샷이 저장되었습니다!"
    },
    "Ελληνικά": {
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
    }
}

def get_text(language, text_key):
    return translations.get(language, {}).get(text_key, text_key)
