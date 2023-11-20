import tkinter as tk
import mss
import os
import datetime
from PIL import Image
import time

def take_screenshots():
    # 창 숨기기
    root.withdraw()

    # 창이 완전히 숨겨진 후 스크린샷을 찍기 위해 잠시 대기
    time.sleep(0.5)

    with mss.mss() as sct:
        for monitor_number, monitor in enumerate(sct.monitors[1:], start=1):
            shot = sct.grab(monitor)
            img = Image.frombytes('RGB', (shot.width, shot.height), shot.rgb)

            filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_Monitor_{monitor_number}.png"
            img.save(os.path.join('screenshots', filename))

    # 스크린샷 저장 후 창 다시 표시
    root.deiconify()
    label.config(text="Screenshots Saved")

# GUI 설정
root = tk.Tk()
root.title("Screenshot App")
root.geometry("200x130")

if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

button = tk.Button(root, text="Take Screenshots", command=take_screenshots)
button.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()
