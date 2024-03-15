#pyinstaller --onefile code/install/main.py -n "install"
# pyinstaller --onefile code/file_list/main.py -n "file_list"
import os
import sys
import requests
"file_list.config"
app_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp")
app_url = "https://raw.githubusercontent.com:443/dmitry663/FileShareApp/main/app/"

def isdir(folder):
    return os.path.isdir(folder)

def mkdir(folder):
    if isdir(folder):
        pass
    elif isdir("\\".join(folder.split('\\')[:-1])):
        os.mkdir(folder)
    else:
        mkdir("\\".join(folder.split('\\')[:-1]))
        os.mkdir(folder)
def get_file_list(url_path):
    return [file_name for file_name in requests.get(url_path).text.split("\n") if file_name != ""]

def download_file(file_name, app_url, app_path):
    response = requests.get(app_url+file_name)
    mkdir(os.path.dirname(os.path.join(app_path, file_name)))
    write_file(response.content, app_path, file_name)

def write_file(data, file_path, file_name):
    with open(os.path.join(file_path, file_name), 'w') as file:
        file.write(data)
        
def main():
    app_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp")
    app_url = "https://raw.githubusercontent.com:443/dmitry663/FileShareApp/main/app/"

    for file_name in get_file_list(app_url+"file_list.config"):
        download_file(file_name, app_url, app_path)

if __name__ == "__main__":
    main()