import tkinter as tk
import mss
import os
import datetime
from PIL import Image

def take_screenshots():
    with mss.mss() as sct:
        # 모든 모니터에 대한 스크린샷 촬영
        for monitor_number, monitor in enumerate(sct.monitors[1:], start=1): # 첫 번째 항목(전체 화면)은 제외
            shot = sct.grab(monitor)
            img = Image.frombytes('RGB', (shot.width, shot.height), shot.rgb)

            # 현재 시간을 기반으로 파일 이름 생성
            filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_Monitor_{monitor_number}.png"

            # 파일 저장
            img.save(os.path.join('screenshots', filename))

            # 사용자에게 저장 완료 알림
            label.config(text=f"Screenshot Saved: Monitor {monitor_number}")

# GUI 설정
root = tk.Tk()
root.title("Screenshot App")

# 스크린샷 저장 폴더 생성 (없으면)
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# 버튼과 레이블 추가
button = tk.Button(root, text="Take Screenshots", command=take_screenshots)
button.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=10)

# GUI 실행
root.mainloop()