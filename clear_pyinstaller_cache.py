import os
import shutil

# 获取当前用户的用户名
username = os.getlogin()
# 拼接缓存文件夹的路径
temp_path = f"C:\\Users\\{username}\\AppData\\Local\\Temp"
# 遍历缓存文件夹中的所有文件和文件夹
for item in os.listdir(temp_path):
    # 如果是以tmp开头的文件夹，就删除它
    if item.startswith("tmp"):
        # 拼接完整的文件夹路径
        folder_path = os.path.join(temp_path, item)
        # 删除文件夹及其内容
        shutil.rmtree(folder_path)
