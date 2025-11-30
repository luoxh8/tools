import os
import sys
import time

from DrissionPage import WebPage, ChromiumOptions


def shutdown_computer():
    """执行关机命令"""
    print("程序执行完成，准备关机...")
    time.sleep(3)  # 给用户3秒时间取消
    if sys.platform == "win32":
        os.system("shutdown /s /t 1")
    elif sys.platform == "darwin":  # macOS
        os.system("sudo shutdown -h now")
    else:  # Linux
        os.system("sudo shutdown -h now")


def countdown(t):
    for i in range(t, 0, -1):
        print(f"倒计时: {i} 秒", end='\r')
        time.sleep(1)
    print("时间到！")


def calculate_seconds_until_end(current_time_str, total_duration_str):
    def time_str_to_seconds(time_str):
        parts = time_str.split(':')
        if len(parts) == 3:
            hours = int(parts[0])
            minutes = int(parts[1])
            seconds = int(parts[2])
            return hours * 3600 + minutes * 60 + seconds
        elif len(parts) == 2:
            minutes = int(parts[0])
            seconds = int(parts[1])
            return minutes * 60 + seconds
        else:
            raise ValueError("时间格式应为 '分:秒' 或 '时:分:秒'")

    current_seconds = time_str_to_seconds(current_time_str)
    total_seconds = time_str_to_seconds(total_duration_str)
    seconds_until_end = total_seconds - current_seconds
    return max(0, seconds_until_end)


def start_auto_play(page):
    try:
        for el in page.eles('@class=contentItem'):
            if el('text=已观看'):
                pass
            else:
                print('===开始播放===')
                print(el('@class=itemTitle').text)
                el('@class=itemText').click()
                tab = page.get_tab(page.latest_tab)
                time.sleep(5)

                current_time = tab.ele('@|class=played-time@|class=ccH5TimeCurrent').text
                total_duration = tab.ele('@|class=total-time@|class=ccH5TimeTotal').text
                remaining_seconds = calculate_seconds_until_end(current_time, total_duration)
                remaining_seconds += 1
                print(f'当前播放进度为 {current_time}')
                print(f'总时长为 {total_duration}')
                print(f'剩余 {remaining_seconds}s 结束')
                countdown(remaining_seconds)
                tab.close()
                print('===结束播放===')

        # 所有视频播放完成后自动关机
        shutdown_computer()

    except Exception as e:
        print(f"程序出错: {e}")
        print("准备自动关机...")
        shutdown_computer()


# 主程序
try:
    co = ChromiumOptions()
    co.set_browser_path(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
    page = WebPage(chromium_options=co)

    # page.get("https://xxzpx.91huayi.com/exercise/ExerciseHome/index")
    start_auto_play(page)

except Exception as e:
    print(f"程序执行出错: {e}")
    shutdown_computer()
