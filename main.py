import tkinter as tk
from PIL import ImageGrab
import pyautogui
import os
import datetime


def take_screenshot():
    # 현재 시간을 기반으로 파일 이름 생성
    filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"

    # 스크린샷 촬영
    screenshot = pyautogui.screenshot()

    # 파일 저장
    screenshot.save(os.path.join('screenshots', filename))

    # 사용자에게 저장 완료 알림
    label.config(text="Screenshot Saved: " + filename)


# GUI 설정
root = tk.Tk()
root.title("Screenshot Spliter")

# 스크린샷 저장 폴더 생성 (없으면)
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# 버튼과 레이블 추가
button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
button.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=10)

# GUI 실행
root.mainloop()
