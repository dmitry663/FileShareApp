import os
import subprocess

# 실행 파일 경로
executable_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp", "service.exe")

# 결과를 저장할 파일 경로
output_file_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Dmitry663", "FileShareApp", "output.txt")

# 실행 파일 실행 및 결과를 파일에 추가
with open(output_file_path, "a") as output_file:
    subprocess.run([executable_path], stdout=output_file, stderr=subprocess.PIPE)

print("실행 파일의 결과가", output_file_path, "파일에 추가되었습니다.")
