import hashlib
import os
import shutil
from pathlib import Path
from datetime import datetime
import exifread
from PIL import Image
import filetype

def calculate_md5(file_path):
    """计算文件MD5哈希值（优化大文件处理）[6,7](@ref)"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_media_date(file_path):
    """获取媒体文件拍摄日期（增强兼容性）[3](@ref)"""
    file_path = str(file_path)
    try:
        file_type = filetype.guess(file_path)
        if file_type is None:
            return datetime.fromtimestamp(os.path.getmtime(file_path))
    except Exception:
        return datetime.fromtimestamp(os.path.getmtime(file_path))

    if file_type.mime.startswith('image/'):
        try:
            with open(file_path, 'rb') as f:
                tags = exifread.process_file(f, stop_tag='DateTimeOriginal')
                if tags.get('EXIF DateTimeOriginal'):
                    return datetime.strptime(str(tags['EXIF DateTimeOriginal']), '%Y:%m:%d %H:%M:%S')
        except Exception:
            pass
        try:
            with Image.open(file_path) as img:
                exif_data = img._getexif()
                if exif_data and 36867 in exif_data:
                    return datetime.strptime(exif_data[36867], '%Y:%m:%d %H:%M:%S')
        except Exception:
            pass

    try:
        if os.name == 'nt':
            creation_time = os.path.getctime(file_path)
        else:
            stat = os.stat(file_path)
            creation_time = getattr(stat, 'st_birthtime', stat.st_mtime)
        return datetime.fromtimestamp(creation_time)
    except Exception:
        return datetime.fromtimestamp(os.path.getmtime(file_path))

def dedup_and_organize_multi(source_dirs, target_dir):
    """
    多目录去重整理核心功能[1,3](@ref)
    - source_dirs: 源目录路径列表
    - target_dir: 输出目录路径
    """
    unique_hashes = set()
    os.makedirs(target_dir, exist_ok=True)
    processed_count = 0
    error_count = 0
    media_extensions = {'.jpg', '.jpeg', '.png', '.heic', '.mov', '.mp4', '.avi', '.bmp', '.tiff', '.webp', '.mkv', '.3gp'}

    for source_dir in source_dirs:  # 遍历每个源目录[3](@ref)
        source_path = Path(source_dir)
        if not source_path.exists():
            print(f"警告：源目录不存在 {source_dir}，已跳过")
            continue
        for file_path in source_path.rglob('*'):  # 递归遍历[1](@ref)
            if file_path.is_file() and file_path.suffix.lower() in media_extensions:
                try:
                    file_hash = calculate_md5(file_path)
                    if file_hash in unique_hashes:  # 全局去重[6,7](@ref)
                        continue
                    unique_hashes.add(file_hash)

                    date_taken = get_media_date(file_path)
                    year_month = date_taken.strftime("%Y/%Y-%m")
                    target_subdir = Path(target_dir) / year_month
                    target_subdir.mkdir(parents=True, exist_ok=True)

                    base_name = date_taken.strftime("%Y%m%d_%H%M%S")
                    new_filename = base_name + file_path.suffix.lower()
                    final_target = target_subdir / new_filename
                    counter = 1
                    while final_target.exists():  # 处理重名冲突[1,4](@ref)
                        new_filename = f"{base_name}_{counter:02d}{file_path.suffix.lower()}"
                        final_target = target_subdir / new_filename
                        counter += 1

                    shutil.copy2(file_path, final_target)  # 保留元数据[1](@ref)
                    processed_count += 1
                    print(f"已处理: {file_path} -> {final_target}")
                except Exception as e:
                    error_count += 1
                    print(f"错误处理 {file_path}: {e}")

    print(f"整理完成！成功处理 {processed_count} 个文件，{error_count} 个错误。")

if __name__ == "__main__":
    source_folders = [  # 支持多个源目录[3](@ref)
        r"D:\games\ios\v1",
        r"D:\games\ios\v2",
        r"D:\games\ios\v3",
        r"D:\games\ios\v4",
        r"D:\games\ios\v5",
    ]
    target_folder = r"D:\games\ios\out"
    dedup_and_organize_multi(source_folders, target_folder)