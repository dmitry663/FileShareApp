import file
from flask import Flask, request, redirect

app = Flask(__name__)

@app.before_request
def url_cleanup():
    if '//' in request.path:
        return redirect(request.path.replace('//', '/'))
    if request.path.endswith('/') and len(request.path) > 1:
        return redirect(request.path[:-1])    
    
@app.route('/')
def home():
    return file.home()

@app.route('/directory', strict_slashes=False)
def show_folders_root():
    return file.show_folders()

@app.route('/directory/<path:folders>', strict_slashes=False)
def show_folders(folders):
    return file.show_folders(folders)

@app.route('/download', strict_slashes=False)
def download_root():
    return file.download()

@app.route('/download/<path:path>', strict_slashes=False)
def download(path):
    return file.download(path)
    
@app.route('/upload/file', methods=['POST'], strict_slashes=False)
def upload_file_root():
    return file.upload_file()

@app.route('/upload/file/<path:folders>', methods=['POST'], strict_slashes=False)
def upload_file(folders):
    return file.upload_file(folders)

@app.route('/delete/file/<path:path>', strict_slashes=False)
def delete(path):
    return file.delete(path)

@app.route('/add/folder', methods=['POST'], strict_slashes=False)
def add_folder_root():
    new_folders = request.form.get('folder_name')
    return file.add_folder("", new_folders)

@app.route('/add/folder/<path:folders>', methods=['POST'], strict_slashes=False)
def add_folder(folders):
    new_folders = request.form.get('folder_name')
    print(new_folders)
    return file.add_folder(folders, new_folders)

def main(host_name, server_port, service_folder):
    app.run(host=host_name, port=server_port)
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
