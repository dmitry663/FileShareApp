import os

def isdir(folder):
    return os.path.isdir(folder)

def mkdir(folder):
    if isdir(folder):
        pass
    elif isdir(os.path.splitdrive(folder)[0]):
        os.mkdir(folder)
    else:
        mkdir(os.path.splitdrive(folder)[0])
        os.mkdir(folder)

# 테스트
service_folder = "D:\\Users\\Username\\Documents\\ServiceFolder"
print(os.path.splitdrive(service_folder)[0])
