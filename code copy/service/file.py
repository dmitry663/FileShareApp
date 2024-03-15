import os
import env
import arg

from zipfile import ZipFile
from jinja2 import Environment, FileSystemLoader
from flask import request, url_for, send_from_directory, redirect

class FileSystemItem:
    def __init__(self, name, is_directory, size=None):
        self.name = name
        self.is_directory = is_directory
        self.size = size

def open_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    else:
        return file_path
    
"""
from jinja2 import Template
def custom_render_template(template_path, **context):
    template = Template(open_file(template_path))
    return template.render(**context)
"""

def custom_render_template(template_path, **context):
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
    env.globals.update(url_for=url_for)
    env.globals.update(clean_up_path=clean_up_path)
    template = env.get_template(os.path.basename(template_path))
    return template.render(**context)

def get_items(path):
    items = os.listdir(path)
    
    # 폴더와 파일을 먼저 정렬하고, 그 후에 글자순으로 정렬
    folders = sorted([item for item in items if os.path.isdir(os.path.join(path, item))])
    files = sorted([item for item in items if not os.path.isdir(os.path.join(path, item))])
    
    items_list = []
    
    # 폴더에 대한 정보를 가져오기
    for folder in folders:
        folder_path = os.path.join(path, folder)
        folder_size = sum(os.path.getsize(os.path.join(folder_path, file)) for file in os.listdir(folder_path))
        items_list.append(FileSystemItem(name=folder, is_directory=True, size=folder_size))
    
    # 파일에 대한 정보를 가져오기
    for file in files:
        file_path = os.path.join(path, file)
        file_size = os.path.getsize(file_path)
        items_list.append(FileSystemItem(name=file, is_directory=False, size=file_size))

    return items_list

def clean_up_path(path):
    while '//' in path:
        path = path.replace('//', '/')
    if path.endswith('/') and len(request.path) > 1:
        path = path[:-1]
    return path

def zip_folder(folder_path):
    try:
        if not os.path.isdir(os.path.join(env.templates_folder_path, "cache")):
            os.mkdir(os.path.join(env.templates_folder_path, "cache"))

        zip_path = os.path.join(env.templates_folder_path, "cache", "temp.zip")

        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")

        # 폴더 내용을 압축 파일로 생성
        with ZipFile(zip_path, 'w') as zip_file:
            for foldername, subfolders, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    arcname = os.path.relpath(file_path, folder_path)
                    zip_file.write(file_path, arcname)

    except Exception as e:
        # 오류가 발생하면 예외를 캐치하고 출력
        print(f"An error occurred: {e}")

def home():
    return open_file(env.templates_file("home.html"))
    
def show_folders(path = ""):
    return custom_render_template(env.templates_file("show_folders.html"), path = path, items = get_items(arg.service_folder(path)))

def download(path = ""):
    full_path = arg.service_folder(path)
    if os.path.isfile(full_path):
        return download_file(full_path)
    elif os.path.isdir(full_path):
        return download_folder(full_path)
    else:
        return f"File not found: {path}"

def download_file(file_path):
    return send_from_directory(os.path.dirname(file_path), os.path.basename(file_path), as_attachment=True)

def download_folder(folder_path):
    zip_folder(folder_path)
    return send_from_directory(os.path.dirname(env.templates_file(os.path.join("cache","temp.zip"))), os.path.basename(env.templates_file(os.path.join("cache","temp.zip"))), as_attachment=True)

def upload_file(folders=""):
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)
    
    if folders == "":
        file.save(os.path.join(arg.service_folder_path, file.filename))
    else:
        file.save(os.path.join(arg.service_folder_path, folders, file.filename))

    return "upload_file"

def delete(path=""):
    full_path = arg.service_folder(path)
    if os.path.isfile(full_path):
        delete_file(full_path)
    elif os.path.isdir(full_path):
        delete_folder(full_path)
    return "delete"

def delete_file(file_path):
    try:
        os.remove(file_path)
        # print(f"{file_path}를 삭제했습니다.")
    except FileNotFoundError:
        # print(f"{file_path}를 찾을 수 없습니다.")
        pass

def delete_folder(folder_path):
    try:
        os.rmdir(folder_path)
        # print(f"{folder_path}를 삭제했습니다.")
    except FileNotFoundError:
        # print(f"{folder_path}를 찾을 수 없습니다.")
        pass
    except OSError:
        # print(f"{folder_path}는 비어있지 않거나 권한이 없어 삭제할 수 없습니다.")
        pass

def add_folder(folders, new_folders):
    if folders == "":
        full_path = os.path.join(arg.service_folder_path, new_folders)
    else:
        full_path = os.path.join(arg.service_folder_path, folders, new_folders)
    print(os.path.join(arg.service_folder_path, new_folders))
    os.mkdir(full_path)
    return "add_folder"
