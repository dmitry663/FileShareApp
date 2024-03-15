import os
import argparse

parser = argparse.ArgumentParser(description="File Share App")
parser.add_argument('-p', '--port', type=int, help='서버 포트')
parser.add_argument('-v', '--path', type=str, help='서버 폴더 주소')

args = parser.parse_args()

if args.port:
    server_port = args.port
else:
    server_port = 5000

if args.path:
    service_folder_path = args.path
else:
    service_folder_path = os.path.join(os.path.expanduser("~"), "Documents", "Dmitry663", "FileShareApp")

print("서버 포트:", server_port)
print("서버 폴더 주소:", service_folder_path)

service_folder = lambda folder: os.path.join(service_folder_path, folder)