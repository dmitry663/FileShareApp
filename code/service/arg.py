import os

service_folder_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp")

server_port = 5000

service_folder = lambda folder: os.path.join(service_folder_path, folder)