# pyinstaller --onefile code/service/main.py -n "service"

import env
import arg
import app
import socket
import sys
import os

def isdir(folder):
    return os.path.isdir(folder)

def mkdir(folder):
    try:
        if isdir(folder):
            pass
        elif isdir("\\".join(folder.split('\\')[:-1])):
            os.mkdir(folder)
        else:
            mkdir("\\".join(folder.split('\\')[:-1]))
            os.mkdir(folder)
    except OSError as e:
        print(f"디렉토리 생성 중 오류가 발생했습니다: {e}")
        sys.exit(1)

def check_port_in_use(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("localhost", port))
    except socket.error as e:
        if e.errno == socket.errno.EADDRINUSE:
            print(f"포트 {port}는 이미 사용 중입니다.")
            sys.exit(1)
    finally:
        s.close()

def main():
    host_name = env.host_name
    server_port = arg.server_port
    service_folder = arg.service_folder_path
    check_port_in_use(server_port)
    mkdir(service_folder)
    app.main(host_name, server_port, service_folder)

if __name__ == '__main__':
    main()
    