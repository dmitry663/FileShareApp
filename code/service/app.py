import file
from flask import Flask, request, redirect


app = Flask(__name__)

#app.jinja_env.globals.update(clean_up_path=clean_up_path)

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

"""
@app.route('/directory', strict_slashes=False)
def show_folders_root():
    return app.show_folders()

@app.route('/directory/<path:folders>', strict_slashes=False)
def show_folders(folders):
    return app.show_folders()

@app.route('/directory/<path:folders>/download', strict_slashes=False)
def download_folders(folders):
    return app.download_folders()

@app.route('/directory/download/<filename>', strict_slashes=False)
def download_file_root(filename):
    return app.download_file()

@app.route('/directory/<path:folders>/download/<filename>', strict_slashes=False)
def download_file(folders, filename):
    return app.download_file()

@app.route('/directory/<path:folders>/upload/file', methods=['POST'], strict_slashes=False)
def upload_file(folders):
    app.upload_file()
    return "upload_file"

@app.route('/directory/<path:folders>/upload/folder', methods=['POST'], strict_slashes=False)
def upload_folder(folders):
    app.upload_folder()
    return "upload_folder"
"""

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
