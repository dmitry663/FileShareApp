def is_number(self):
    try:
        float(self.get())
        return True
    except ValueError:
        return False
        

import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess

file_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp", "FileShareApp.json")
background_app_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp", "background.exe")
command_app_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp", "command.exe")

def show_alert(text):
    messagebox.showinfo("알림", text)

class InputLabel:
    def __init__(self, root, title):
        self.root = root
        
        self.frame = tk.Frame(root)
        self.frame.pack(anchor="w")

        self.label = tk.Label(self.frame, text=f"{title}: ")
        self.label.grid(row=0, column=0)

        self.value = tk.StringVar()
        self.label_value = tk.Label(self.frame, textvariable=self.value, width=30, anchor="w", justify="left")
        self.label_value.grid(row=0, column=1)

    def set(self, text):
        self.value.set(text)

    def get(self):
        return self.value.get()
    
class InputText:
    def __init__(self, root, title):
        self.root = root
        
        self.frame = tk.Frame(root)
        self.frame.pack(anchor="w")

        self.label = tk.Label(self.frame, text=f"{title}: ")
        self.label.grid(row=0, column=0)

        self.entry = tk.Entry(self.frame, width=30)
        self.entry.grid(row=0, column=1)

    def set(self, text):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, text)

    def get(self):
        return self.entry.get()
    
    def is_number(self):
        try:
            float(self.get())
            return True
        except ValueError:
            return False
    
class FolderSelect:
    def __init__(self, root):
        self.root = root
        
        self.frame = tk.Frame(root)
        self.frame.pack(anchor="w")

        label = tk.Label(self.frame, text="폴더: ")
        label.grid(row = 0, column = 0)

        # 선택된 폴더 경로를 표시하는 레이블
        self.value = tk.StringVar()
        self.folder_label = tk.Label(self.frame, textvariable=self.value, width = 30, anchor="w", justify="left")
        self.folder_label.grid(row = 0, column = 1)
        self.value.set("없음")

        # 폴더 선택 버튼
        self.select_button = tk.Button(self.frame, text="폴더 선택", command=self.select_folder)
        self.select_button.grid(row = 0, column = 2)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.set(folder_path)
            # GUI를 가장 위로 가져오기
            self.root.lift()

    def set(self, text):
        self.value.set(text)
    
    def get(self):
        return self.value.get()

class FileShareSet:
    def __init__(self, root, no, ):
        self.root = root
        
        label = tk.Label(self.root, text="설정")
        label.pack(anchor="w")

        self.frame = tk.Frame(root, relief="solid", bd=3)
        self.frame.pack(anchor="w")

        self.no_text = InputLabel(self.frame, "no")
        self.no_text.set(f"제 {no} 서버")
        self.select_folder = FolderSelect(self.frame)
        self.port_text = InputText(self.frame, "포트")

        self.save_button = tk.Button(self.frame, text="저장", command=self.save)
        self.save_button.pack(anchor="w")

    def set(self, no, path, port):
        self.no_text.set(f"제 {no} 서버")
        self.select_folder.set(path)
        self.port_text.set(port)
    
    def get(self):
        port = self.port_text.get()
        path = self.select_folder.get()
        return {"port":port, "path":path}
    
    def save(self):
        data = self.get()
        if not self.port_text.is_number():
            show_alert("포트는 숫자를 입력")
        elif 0 > int(data["port"]) and int(data["port"]) > 65535:
            show_alert("포트는 0 ~ 65535")
        elif not os.path.isdir(data["path"]):
            show_alert("없는 폴더")
        else:
            process = subprocess.Popen([background_app_path, command_app_path, "create", data["port"], data["path"]])


    def refresh():
        pass

class FileShareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("저장소 공유 어플")

        self.file_share_set = FileShareSet(root,0)

def main():
    root = tk.Tk()
    app = FileShareApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
