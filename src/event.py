from langs import get_text


def check_left_monitor(left_monitor):
    left_monitor.set(not left_monitor.get())


def check_right_monitor(right_monitor):
    right_monitor.set(not right_monitor.get())


def update_ui_texts(button1, button2, left_monitor_check, right_monitor_check, current_language):
    button1.config(text=get_text(current_language, "take"))
    button2.config(text=get_text(current_language, "open"))
    left_monitor_check.config(text=get_text(current_language, "left"))
    right_monitor_check.config(text=get_text(current_language, "right"))
