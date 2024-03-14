import os
import sys
import requests

app_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp")

def isdir(folder):
    return os.path.isdir(folder)

def delete_folder_contents(folder_path):
    # 폴더 내의 모든 파일 삭제
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                delete_folder_contents(file_path)  # 재귀적으로 하위 폴더 내의 모든 파일 삭제
                os.rmdir(file_path)  # 폴더 삭제
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {str(e)}")

def main():
    if isdir(app_path):
        delete_folder_contents(app_path)

if __name__ == "__main__":
    main()