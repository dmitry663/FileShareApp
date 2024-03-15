import os

app_main_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp")
folder_path = lambda file_name: os.path.join(app_main_path, file_name)

templates_folder_path =folder_path("templates")
cache_folder_path =folder_path("cache")
host_name = "0.0.0.0"
debug = True

templates_file = lambda file_name: os.path.join(templates_folder_path, file_name)
cache_file = lambda file_name: os.path.join(cache_folder_path, file_name)