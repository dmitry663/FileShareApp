import os
import tkinter as tk
from tkinter import filedialog

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
    
class FolderSelect:
    def __init__(self, root):
        self.root = root
        
        self.frame = tk.Frame(root)
        self.frame.pack(anchor="w")

        label = tk.Label(self.frame, text="폴더: ")
        label.grid(row = 0, column = 0)

        # 선택된 폴더 경로를 표시하는 레이블
        self.value = tk.StringVar()
        self.folder_label = tk.Label(self.frame, text="없음", textvariable=self.value, width = 30, anchor="w", justify="left")
        self.folder_label.grid(row = 0, column = 1)

        # 폴더 선택 버튼
        self.select_button = tk.Button(self.frame, text="폴더 선택", command=self.select_folder)
        self.select_button.grid(row = 0, column = 2)

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.folder_label.config(text=f"{self.folder_path}")
            # GUI를 가장 위로 가져오기
            self.root.lift()

    def set(self, text):
        self.value.set(text)
    
    def get(self):
        return self.folder_path

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

        self.save_button = tk.Button(self.frame, text="저장")
        self.save_button.pack(anchor="w")

    def set(self, no, path, port):
        self.no_text.set(f"제 {no} 서버")
        self.select_folder.set(path)
        self.port_text.set(port)
    
    def get():
        
    def save():
        result = os.popen(command).read()

    def refresh():
        pass

class FileShareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("저장소 공유 어플")

        self.file_share_set = FileShareSet(root,0)

        a = InputLabel(root, "InputLabel")
        a.set("0000")

        self.b = InputText(root, "InputText")
        self.b.set(a.get() + "0000")
        a.set(self.b.get() + "0000")
        
        self.c = FolderSelect(root)
        self.save_button = tk.Button(root, text="저장", command=self.save)
        self.save_button.pack(anchor="w")
    def save(self):
        self.c.set(self.b.get())
        #self.b.set(self.c.get())
        pass
def main():
    root = tk.Tk()
    app = FileShareApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
