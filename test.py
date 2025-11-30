import ctypes
import time
from pathlib import Path

import winsound


def play_system_beep(frequency: int = 1000, duration: int = 1000, max_retries: int = 2) -> bool:
    """
    使用系统扬声器播放蜂鸣声。这是最基础、兼容性最好的方法 [1,4,9](@ref)。

    Args:
        frequency: 声音频率（赫兹），范围 37-32767。
        duration: 持续时间（毫秒）。
        max_retries: 失败时的最大重试次数。

    Returns:
        成功与否。
    """
    for attempt in range(1, max_retries + 2):  # 重试 max_retries 次，共尝试 max_retries+1 次
        try:
            winsound.Beep(frequency, duration)
            print(f"✅ 系统蜂鸣声播放成功 (尝试 {attempt})")
            return True
        except Exception as e:
            print(f"⚠️ 蜂鸣声播放失败 (尝试 {attempt}): {e}")
            if attempt <= max_retries:
                time.sleep(1)  # 重试前等待1秒
    return False


def play_system_sound(sound_name: str = "SystemExclamation", max_retries: int = 1) -> bool:
    """
    播放Windows系统事件声音（如警告声、感叹号声等），用户体验更佳 [9,10](@ref)。

    Args:
        sound_name: 系统声音别名，如 'SystemExclamation', 'SystemAsterisk', 'SystemHand'。
        max_retries: 失败时的最大重试次数。

    Returns:
        成功与否。
    """
    for attempt in range(1, max_retries + 2):
        try:
            # 使用 SND_ALIAS 播放注册表关联的系统声音 [9](@ref)
            winsound.PlaySound(sound_name, winsound.SND_ALIAS)
            print(f"✅ 系统事件音('{sound_name}')播放成功 (尝试 {attempt})")
            return True
        except Exception as e:
            print(f"⚠️ 系统事件音播放失败 (尝试 {attempt}): {e}")
            if attempt <= max_retries:
                time.sleep(1)
    return False


def play_message_beep(sound_type: int = 0xFFFFFFFF) -> bool:
    """
    通过Windows API的 MessageBeep 函数播放声音，提供不同类型的系统提示音 [5,9](@ref)。

    Args:
        sound_type: 声音类型常量。
            0xFFFFFFFF (默认): 简单的“哔”声。
            0x40 (MB_ICONASTERISK): 提示音。
            0x10 (MB_ICONERROR): 错误声音。
            0x30 (MB_ICONWARNING): 警告声音。

    Returns:
        成功与否。
    """
    try:
        # 使用 ctypes 调用 Windows API [5](@ref)
        ctypes.windll.user32.MessageBeep(sound_type)
        print("✅ MessageBeep 提示音已触发")
        return True
    except Exception as e:
        print(f"⚠️ MessageBeep 播放失败: {e}")
        return False


def play_audio_file(file_path: str) -> bool:
    """
    播放指定的本地音频文件（如WAV格式），最灵活且体验最好 [3,10](@ref)。

    Args:
        file_path: 音频文件的完整路径。

    Returns:
        成功与否。
    """
    if not Path(file_path).is_file():
        print(f"❌ 音频文件不存在: {file_path}")
        return False

    try:
        # 使用 winsound 播放WAV文件 [3,10](@ref)
        winsound.PlaySound(file_path, winsound.SND_FILENAME)
        print("✅ 自定义音频文件播放成功")
        return True
    except Exception as e:
        print(f"⚠️ 播放音频文件失败: {e}")
        return False


def play_alert_sound(level: str = "warning", max_retries: int = 2) -> None:
    """
    主警报函数。提供不同级别的提示音，并自动降级尝试以确保可靠性。

    Args:
        level: 警报级别，可选 'info', 'warning', 'error', 'custom'。
              'custom' 需自行准备音频文件并修改下方代码。
        max_retries: 每种方法的最大重试次数。
    """
    print(f"🔊 尝试播放 {level.upper()} 级别提示音...")

    success = False
    if level == "info":
        # 方案1（首选）: 播放系统提示音（如星号音）
        success = play_system_sound("SystemAsterisk", max_retries)
        # 方案2（降级）: 播放OK声音
        if not success:
            success = play_message_beep(0x00000000)
        # 方案3（保底）: 播放标准蜂鸣声
        if not success:
            success = play_system_beep(800, 500, max_retries)  # 较柔和的蜂鸣

    elif level == "warning":
        # 方案1（首选）: 播放系统警告音（如感叹号音）
        success = play_system_sound("SystemExclamation", max_retries)
        # 方案2（降级）: 播放警告声音
        if not success:
            success = play_message_beep(0x00000030)
        # 方案3（保底）: 播放标准蜂鸣声
        if not success:
            success = play_system_beep(1500, 1000, max_retries)  # 较急促的蜂鸣

    elif level == "error":
        # 方案1（首选）: 播放系统错误音（如关键性停止音）
        success = play_system_sound("SystemHand", max_retries)
        # 方案2（降级）: 播放错误声音
        if not success:
            success = play_message_beep(0x00000010)
        # 方案3（保底）: 播放标准蜂鸣声
        if not success:
            success = play_system_beep(2500, 1500, max_retries)  # 高频率长蜂鸣

    elif level == "custom":
        # 播放自定义音频文件（需要您准备一个WAV文件并指定路径）
        custom_sound_path = r"C:\Windows\Media\Alarm01.wav"  # 示例路径，请修改为您的文件路径
        success = play_audio_file(custom_sound_path)

    if success:
        print("✅ 提示音播放流程结束")
    else:
        print("❌ 所有提示音方案均失败，请检查系统音频设置")
        # 此处可以添加其他非声音提醒方式，例如闪烁窗口等


# 测试代码
if __name__ == "__main__":
    print("=== 测试信息音 ===")
    play_alert_sound("info")
    time.sleep(2)

    print("\n=== 测试警告音 ===")
    play_alert_sound("warning")
    time.sleep(2)

    print("\n=== 测试错误音 ===")
    play_alert_sound("error")
    time.sleep(2)
