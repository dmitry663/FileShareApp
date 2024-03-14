import os
import env
from jinja2 import Template

def open_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    else:
        return file_path

def home():
    return open_file(env.templates_file("home.html"))
    
def show_folders():
    return open_file(env.templates_file("home.html"))



"""

import os
from jinja2 import Template
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, send_file

class FileSystemItem:
    def __init__(self, name, is_directory, size=None):
        self.name = name
        self.is_directory = is_directory
        self.size = size

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

def zip_folder(folder_path, zip_path):
    try:
        # 폴더 경로와 압축 파일 경로를 절대 경로로 정규화
        folder_path = os.path.abspath(folder_path)
        zip_path = os.path.abspath(zip_path)

        # 폴더 경로가 존재하는지 확인
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

def clean_up_path(path):
    while '//' in path:
        path = path.replace('//', '/')
    if path.endswith('/') and len(request.path) > 1:
        path = path[:-1]
    return path

def custom_render_template(template_path, **context):
    with open(template_path, 'r', encoding='utf-8') as file:
        template_string = file.read()
    template = Template(template_string)
    rendered_template = template.render(**context)

    return rendered_template


"""