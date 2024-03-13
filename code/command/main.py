import os
import sys
import json

file_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp", "gui.exe")

def save_json(data, file_path = file_path):
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile)

def initialize():
    if os.path.isfile(file_path):
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
    else:
        data = {}
        data['size'] = 5
        data['count'] = 0
        data['state'] = 0
        data['token'] = []
        save_json(data)
    return data

def start():
    pass

def stop():
    pass

def create(path, port):
    data = initialize()
    if data['count'] < data['size']:
        data['count'] += 1
        data['token'].append({"path":path, "port":port, "run":False})
        save_json(data)

def rm(no):
    data = initialize()
    if no < data['count']:
        data['count'] -= 1
        del data['token'][no]
        save_json(data)

def modify():
    pass

def boot():
    pass





def main():
    if len(sys.argv)<2:
        print("옵션을 선택해 주세요. -h 또는 --help를 추가하여 옵션을 확인 할 수 있습니다. 하지만 지금은 추가 안됨.")
    elif sys.argv[1] in ["-h", "--help"]:
        pass
    elif sys.argv[1] in ["boot"]:
        pass
    elif sys.argv[1] in ["ps"]:
        if len(sys.argv)<3:
            # 현재 실행 중인 프로세스
            pass
        elif sys.argv[2] in ["-a"]:
            # 모든 프로세스
            pass
        else:
            # 잘못된 경우
            pass
    elif sys.argv[1] in ["stop"]:
        if len(sys.argv)<3:
            # 잘못된 경우
            pass
        else:
            for pin in sys.argv[2:]:
                #stop(pin)
                pass
    elif sys.argv[1] in ["start"]:
        if len(sys.argv)<3:
            # 잘못된 경우
            pass
        else:
            for pin in sys.argv[2:]:
                #stop(pin)
                pass
        pass
    elif sys.argv[1] in ["rm"]:
        pass
    elif sys.argv[1] in ["create"]:

        pass
    elif sys.argv[1] in ["modify"]:
        pass
    else:
        pass


if __name__=="__main__":
    main()
