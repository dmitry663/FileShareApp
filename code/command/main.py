import os
import sys
import json
import subprocess
import psutil

file_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp", "FileShareApp.json")
background_app_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp", "background.exe")
service_app_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp", "service.exe")
class FileShareApp:
    def __init__(self, data):
        self.size = data['size']
        self.count = data['count']
        self.token = [Bio(token) for token in data['token']]

    def get(self):
        return {'size':self.size, 'count':self.count, 'token':[token.get() for token in self.token]}
class Bio:
    def __init__(self, data):
        self.path = data["path"]
        self.port = data["port"]
        self.run = data["run"]

    def get(self):
        return {'path':self.path, 'port':self.port, 'run':self.run}

def save_json(data, file_path = file_path):
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile)

def read_json(file_path):
    data = None
    if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
    return data

def initialize():
    json_data = read_json(file_path)
    if json_data:
        data = FileShareApp(json_data)
    else:
        data = FileShareApp({'size':5, 'count':0, 'token':[]})
        save_json(data.get())
    return data

def ps():
    data = initialize()
    for token in data.token:
        print("실행중" if token.run else "----", token.port, token.path)

def create(path, port):
    if 0 <= port <= 65535 and os.path.isdir(path):
        data = initialize()
        if len(data.token) < data.size:
            data.token.append(Bio({"path":path, "port":port, "run":False}))
            save_json(data.get())
        else:
            print("생성할 수 있는 토큰을 넘었음")
    elif 0 > port or port > 65535:
        print("포트 범위 초과 0 ~ 65535")
    elif not os.path.isdir(path):
        print("디렉토리 없음")

def rm(no):
    data = initialize()
    if no < len(data.token) and data.token[no].run == False:
        del data.token[no]
        save_json(data.get())
    elif not no < len(data.token):
        print("토큰 범위 초과")
    elif data.token[no].run == True:
        print("토큰이 실행 중")

def modify(no, port):
    data = initialize()
    if no < len(data.token) and data.token[no].run == False:
        data.token[no].port = port
        save_json(data.get())
    elif not no < len(data.token):
        print("토큰 범위 초과")
    elif data.token[no].run == True:
        print("토큰이 실행 중")

def start(no):
    data = initialize()
    if no < len(data.token) and data.token[no].run == False:
        data.token[no].run = True
        data.count += 1
        save_json(data.get())
        process = subprocess.Popen([background_app_path, service_app_path, "-p", data.token[no].port, "-v", data.token[no].path])
    elif not no < len(data.token):
        print("토큰 범위 초과")
    elif data.token[no].run == True:
        print("토큰이 실행 중")

def stop(no):
    data = initialize()
    if no < len(data.token) and data.token[no].run == True:
        for proc in psutil.process_iter(['pid', 'cmdline']):
            if proc.info['cmdline'] and " ".join([service_app_path, "-p", data.token[no].port, "-v", data.token[no].path]) in ' '.join(proc.info['cmdline']):
                # 해당 명령어를 실행한 프로세스 종료
                proc.terminate()
        data.token[no].run = False
        data.count -= 1
        save_json(data.get())
    elif not no < len(data.token):
        print("토큰 범위 초과")
    elif data.token[no].run == False:
        print("토큰이 실행 중이 아님")

def boot():
    data = initialize()
    if data.count:
        for token in data.token:
            if token.run:
                stop(data.token.index(token))
                start(data.token.index(token))

def main():
    if len(sys.argv)<2:
        print("옵션을 선택해 주세요. -h 또는 --help를 추가하여 옵션을 확인 할 수 있습니다. 하지만 지금은 추가 안됨.")
    elif sys.argv[1] in ["-h", "--help"]:
        pass
    elif sys.argv[1] in ["boot"]:
        boot()
    elif sys.argv[1] in ["ps"]:
        ps()
    elif sys.argv[1] in ["start"]:
        start(int(sys.argv[2]))
    elif sys.argv[1] in ["stop"]:
        stop(int(sys.argv[2]))
    elif sys.argv[1] in ["rm"]:
        rm(int(sys.argv[2]))
    elif sys.argv[1] in ["create"]:
        create(sys.argv[3], int(sys.argv[2]))
    elif sys.argv[1] in ["modify"]:
        modify(int(sys.argv[2]), int(sys.argv[3]))
    else:
        pass


if __name__=="__main__":
    main()
