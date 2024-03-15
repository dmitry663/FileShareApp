# pyinstaller --onefile code/file_list/main.py -n "file_list"
import os

def get_file_list(base_path = "."):
    file_list = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_list.append(os.path.relpath(os.path.join(root, file), base_path))
        
    return file_list

def write_file(data, file_path = ".", file_name = "output.txt"):
    with open(os.path.join(file_path, file_name), 'w') as file:
        file.write(data)

def main():
    write_file('\n'.join(get_file_list()), file_name = "file_list.config")

if __name__ == "__main__":
    main()