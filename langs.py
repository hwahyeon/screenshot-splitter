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
        "create": "Created by",
        "success": "Screenshots Saved!",
        "lang_change_title": "Language Changed",
        "lang_change_cont": "Selected language: ",
        "folder_change_title": "Folder Selected",
        "folder_change_cont": "Selected Folder: "
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
        "create": "만든 이",
        "success": "스크린샷이 저장되었습니다!",
        "lang_change_title": "언어 변경",
        "lang_change_cont": "언어가 변경되었습니다: ",
        "folder_change_title": "저장 위치 변경",
        "folder_change_cont": "저장 위치가 변경되었습니다: "
    },
    "Ελληνικά": {
        "settings": "Ρυθμίσεις",
        "folder": "Αλλαγή φακέλου αποθήκευσης",
        "language": "Γλώσσα",
        "exit": "Έξοδος",
        "help": "Βοήθεια",
        "about": "Πληροφορίες",
        "close": "Κλείσιμο",
        "left": "Αριστερή οθόνη (L)",
        "right": "Δεξιά οθόνη (R)",
        "take": "Λήψη στιγμιότυπων οθόνης (Alt+Z)",
        "open": "Ανοίξτε τον φάκελο (Alt+O)",
        "create": "Δημιουργός",
        "success": "Αποθηκεύτηκε!",
        "lang_change_title": "Η γλώσσα άλλαξε",
        "lang_change_cont": "Επιλεγμένη γλώσσα: ",
        "folder_change_title": "Επιλεγμένος φάκελος",
        "folder_change_cont": "Επιλεγμένος φάκελος: "
    }
}


def get_text(language, text_key):
    return translations.get(language, {}).get(text_key, text_key)
