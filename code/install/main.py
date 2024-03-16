# pyinstaller --onefile code/install/main.py -n "install"

import os
import requests

def isdir(folder):
    return os.path.isdir(folder)

def mkdir(folder):
    if os.path.exists(os.path.splitdrive(folder)[0]):
        if isdir(folder):
            pass
        elif isdir("\\".join(folder.split('\\')[:-1])):
            os.mkdir(folder)
        else:
            mkdir("\\".join(folder.split('\\')[:-1]))
            os.mkdir(folder)
    else:
        raise ValueError(f"{os.path.splitdrive(folder)[0]} 드라이브가 존재하지 않습니다.")

def get_file_list(url_path):
    return [file_name for file_name in requests.get(url_path).text.split("\n") if file_name != ""]

def download_file(file_name, app_url, app_path):
    response = requests.get(clean_url(app_url+file_name))
    mkdir(os.path.dirname(os.path.join(app_path, file_name)))
    write_file(response.content, app_path, file_name)

def write_file(data, file_path, file_name):
    with open(os.path.join(file_path, file_name), 'wb') as file:
        file.write(data)

def create_empty_file(file_path):
    try:
        with open(file_path, 'w'):
            pass
        print(f"빈 파일이 생성되었습니다: {file_path}")
    except OSError as e:
        print(f"빈 파일 생성 중 오류가 발생했습니다: {e}")

def clean_url(url):
    return url.replace('\\', '/')

def main():
    app_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp")
    app_url = "https://raw.githubusercontent.com:443/dmitry663/FileShareApp/main/app/"

    if not os.path.isfile(os.path.join(app_path, 'end.config')):
        for file_name in get_file_list(app_url+"file_list.config"):
            print(app_url+file_name)
            print(os.path.join(app_path, file_name))
            download_file(file_name, app_url, app_path)
        create_empty_file(os.path.join(app_path, 'end.config'))

if __name__ == "__main__":
    main()