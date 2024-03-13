#pyinstaller -w --onefile code/switch/main.py -n "switch"
import os
import sys
import subprocess


gui_app_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp", "gui.exe")
command_app_path =  os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp", "command.exe")

def main():
    if len(sys.argv) > 1:
        process = subprocess.Popen([command_app_path] + sys.argv[1:])
    else:
        process = subprocess.Popen(gui_app_path)

if __name__=="__main__":
    main()
