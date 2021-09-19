from time import sleep

import keyboard as keyboard
import pyautogui


def print_current_xy():
    x, y = pyautogui.position()
    print(x, y)


def auto_win_condition():
    pyautogui.FAILSAFE = True
    pyautogui.hotkey('alt', 'tab')
    sleep(1)
    pyautogui.click(1500, 649, button='left')
    pyautogui.click(1924, 823, button='left')
    pyautogui.hotkey('alt', 'tab')


keyboard.add_hotkey('f1', auto_win_condition)
keyboard.add_hotkey('f2', print_current_xy)
keyboard.wait("esc")
