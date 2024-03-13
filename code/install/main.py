import os
import sys
import os.path
import requests

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

def main():
    if not os.path.isfile(os.path.join(app_path, 'end.config')):
        for file_name in requests.get(app_url+"config.txt").text.split("\n"):
            response = requests.get(app_url+file_name)
            mkdir(os.path.dirname(os.path.join(app_path, file_name)))
            with open(os.path.join(app_path, file_name), 'wb') as file:
                file.write(response.content)


    if len(sys.argv) > 1:
        print([arg for arg in sys.argv])
        #os.system('"C:/Windows/System32/notepad.exe"')
    # 명령 여부
    # 명령

    elif len(sys.argv) == 1:
        print(sys.argv[0])
        #os.system('"C:/Windows/System32/notepad.exe"')
    
    # 자식 프로세스 실행
    #import subprocess
    #process = subprocess.Popen(["python", "child_process.py"])

if __name__ == "__main__":
    main()