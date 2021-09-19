import pyautogui
import win32gui

top_windows = []
win32gui.EnumWindows(
    lambda hwnd, top_windows: top_windows.append((hwnd, win32gui.GetWindowText(hwnd))),
    top_windows,
)


def click_pic(image_name):
    location = pyautogui.locateOnScreen(image=image_name, confidence=0.7)
    while location is None: location = pyautogui.locateOnScreen(image_name)
    pyautogui.moveTo(location)
    pyautogui.click()


def show_lol_to_front():
    for i in top_windows:
        if "league" in i[1].lower():
            win32gui.ShowWindow(i[0], 5)
            win32gui.SetForegroundWindow(i[0])
            break


show_lol_to_front()
click_pic("find_game.png")
click_pic("accept.png")
