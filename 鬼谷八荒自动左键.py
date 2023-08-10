import pyautogui
import time

# 设置变量以跟踪鼠标左键的状态
left_mouse_button_pressed = False

while True:
    # 检查鼠标左键是否被按下
    if pyautogui.mouseDown(button='left'):
        # 如果鼠标左键被按下，等待1秒
        time.sleep(1)
        # 如果鼠标左键仍然被按下，模拟长按鼠标左键
        if pyautogui.mouseDown(button='left'):
            left_mouse_button_pressed = True
            pyautogui.mouseDown(button='left')
    # 如果鼠标左键已经长按，检查是否再次点击鼠标左键
    elif left_mouse_button_pressed and pyautogui.mouseDown(button='left'):
        # 如果再次点击鼠标左键，取消长按状态
        left_mouse_button_pressed = False
        pyautogui.mouseUp(button='left')
