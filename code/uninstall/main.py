# pyinstaller --onefile code/uninstall/main.py -n "uninstall"

import os
import shutil

def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"폴더가 삭제되었습니다: {folder_path}")
    except OSError as e:
        print(f"폴더 삭제 중 오류가 발생했습니다: {e}")

def main():
    app_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp")
    delete_folder(app_path)

if __name__ == "__main__":
    main()