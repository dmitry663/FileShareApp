import os
import tkinter as tk
from tkinter import filedialog


class FolderSelect:
    def __init__(self, root):
        self.root = root
        
        self.frame = tk.Frame(root)
        self.frame.pack(anchor="w")

        label = tk.Label(self.frame, text="폴더: ")
        label.grid(row = 0, column = 0)

        # 선택된 폴더 경로를 표시하는 레이블
        self.folder_label = tk.Label(self.frame, text="없음", width = 30, anchor="w", justify="left")
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
    
    def get(self):
        return self.folder_path

class InputText:
    def __init__(self, root, title):
        self.root = root
        
        self.frame = tk.Frame(root)
        self.frame.pack(anchor="w")

        label = tk.Label(self.frame, text=f"{title}: ")
        label.grid(row = 0, column = 0)

        self.entry = tk.Entry(self.frame, width = 30)
        self.entry.grid(row = 0, column = 1)

    def set(self, text):
        self.entry.insert(0, f"{text}")

    def get(self):
        return self.entry.get()
    
class InputLabel:
    def __init__(self, root, title):
        self.root = root
        
        self.frame = tk.Frame(root)
        self.frame.pack(anchor="w")

        label = tk.Label(self.frame, text=f"{title}: ")
        label.grid(row = 0, column = 0)

        self.label = tk.Label(self.frame, text="", width = 30, anchor="w", justify="left")
        self.label.grid(row = 0, column = 1)

    def set(self, text):
        self.label.config(text=f"{text}")

    def get(self):
        return self.label.cget()
    
    
    

    
class FileShareMgt:
    def __init__(self, root, ):
        self.root = root

        self.frame = tk.Frame(root, relief="solid", bd=3)
        self.frame.pack(anchor="w")
        
        self.frame1 = tk.Frame(self.frame)
        self.frame1.grid(row = 0, column = 0)

        self.no_text = InputLabel(self.frame1, "no")
        self.no_text.set(f"제 {0} 서버")
        self.select_folder = InputLabel(self.frame1, "폴더")
        self.select_folder.set(f"제 {0} 서버")
        self.port_text = InputLabel(self.frame1, "포트")
        self.port_text.set(f"제 {0} 서버")

        self.frame2 = tk.Frame(self.frame)
        self.frame2.grid(row = 0, column = 1)

        self.save_button = tk.Button(self.frame2, text="수정")
        self.save_button.pack(anchor="w")
        self.save_button = tk.Button(self.frame2, text="시장")
        self.save_button.pack(anchor="w")
        self.save_button = tk.Button(self.frame2, text="삭제")
        self.save_button.pack(anchor="w")
    
class FileShareMgts:
    def __init__(self, root, ):
        self.root = root
        
        label = tk.Label(self.root, text="관리")
        label.pack(anchor="w")

        self.frame = tk.Frame(root, relief="solid", bd=3)
        self.frame.pack(anchor="w")

        self.no_text = InputLabel(self.frame, "no")
        self.no_text.set(f"제 {0} 서버")
        self.select_folder = FolderSelect(self.frame)
        self.port_text = InputText(self.frame, "포트")

        self.save_button = tk.Button(self.frame, text="저장")
        self.save_button.pack(anchor="w")
    def save():
        pass
    
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

    def save():
        pass

    def refresh():
        pass
    
class FileShareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("저장소 공유 어플")

        self.file_share_set = FileShareSet(root,0)

    def refresh():
        pass




def main():
    root = tk.Tk()
    app = FileShareApp(root)
    root.mainloop()

if __name__=="__main__":
    main()

