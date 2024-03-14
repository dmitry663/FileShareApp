import os

templates_folder_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp", "templates")
debug = True

templates_file = lambda file_name: os.path.join(templates_folder_path, file_name)