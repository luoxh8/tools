from time import sleep

import keyboard as keyboard
import pyautogui


def print_current_xy():
    x, y = pyautogui.position()
    print(x, y)


def auto_win_condition():
    pyautogui.FAILSAFE = True
    pyautogui.hotkey('alt', 'tab')
    sleep(1.5)
    pyautogui.click(1308, 650, button='left')
    pyautogui.click(1948, 908, button='left')
    pyautogui.hotkey('alt', 'tab')


def automatically_end_training():
    pyautogui.FAILSAFE = True
    pyautogui.hotkey('alt', 'tab')
    sleep(1.5)
    pyautogui.click(1716, 913, button='left')
    pyautogui.click(1872, 995, button='left')
    pyautogui.hotkey('alt', 'tab')


keyboard.add_hotkey('f1', auto_win_condition)
keyboard.add_hotkey('f2', automatically_end_training)
keyboard.add_hotkey('f3', print_current_xy)
keyboard.wait("esc")
