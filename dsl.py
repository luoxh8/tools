import platform

if platform.system() == 'Windows':
    import ctypes
    import time

    user32 = ctypes.windll.user32
    screenWidth = user32.GetSystemMetrics(0)
    screenHeight = user32.GetSystemMetrics(1)

    while True:
        ctypes.windll.user32.SetCursorPos(screenWidth, screenHeight)
        ctypes.windll.user32.mouse_event(0x0008, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(0x0010, 0, 0, 0, 0)
        time.sleep(300)

elif platform.system() == 'Darwin':
    import os
    import time

    getScreenSize = "osascript -e 'tell application \"Finder\" to get bounds of window of desktop'"
    screenSize = os.popen(getScreenSize).read()
    screenWidth, screenHeight = screenSize.split(',')[-2:]
    screenWidth, screenHeight = int(screenWidth), int(screenHeight)

    while True:
        moveMouse = f"osascript -e 'tell application \"System Events\" to tell process \"Finder\" to set position of every item of desktop to {{{screenWidth}, {screenHeight}}}'"
        clickMouse = f"osascript -e 'tell application \"System Events\" to click at {{{screenWidth}, {screenHeight}}}'"
        os.system(moveMouse)
        os.system(clickMouse)
        time.sleep(300)
