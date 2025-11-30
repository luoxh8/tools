import os

target_dir = r"D:\games\ios\out"

# 递归统计
file_count = sum(len(files) for _, _, files in os.walk(target_dir))
print(f"总文件数：{file_count}")

# 或者使用pathlib的单行版本
from pathlib import Path
file_count = len(list(Path(target_dir).rglob('*')))
print(f"总文件数：{file_count}")