# pyinstaller -w --onefile code/background_execution/main.py -n "background"

import os
import sys

def execute(executable_path):
    command = f'{" ".join(executable_path)}'
    result = os.popen(command).read()
    return result

def append_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)

def main():
    log_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp", "log.txt")
    if len(sys.argv) < 2:
        print("프로그램을 실행하기 위한 인자가 부족합니다.")
        sys.exit(1)
    append_file(log_path, "###기록###\n\n"+execute(sys.argv[1:]))

if __name__ == "__main__":
    main()