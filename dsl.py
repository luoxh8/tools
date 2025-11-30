import os
import platform
import time


def move_and_click_windows():
    import ctypes
    user32 = ctypes.windll.user32
    screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    user32.SetCursorPos(screen_width - 1, screen_height - 1)
    user32.mouse_event(0x0008, 0, 0, 0, 0)  # 鼠标右键按下
    user32.mouse_event(0x0010, 0, 0, 0, 0)  # 鼠标右键弹起


def move_and_click_macos():
    os.system(f'''osascript -e 'tell application "System Events"
        set screenSize to item 3 of (get bounds of window 1 of application "Finder")
        set theList to {{0, 0}}
        set theList to {{theList}} & {{screenSize - 1, screenSize - 1}}
        set mouseLoc to item 1 of theList
        set xLoc to item 1 of mouseLoc
        set yLoc to item 2 of mouseLoc
        click at {{xLoc, yLoc}}
    end tell' ''')


while True:
    if platform.system() == 'Windows':
        move_and_click_windows()  # 将鼠标移动到屏幕右下角并点击鼠标右键
    elif platform.system() == 'Darwin':
        move_and_click_macos()  # 将鼠标移动到屏幕右下角并点击鼠标右键
    time.sleep(300)
