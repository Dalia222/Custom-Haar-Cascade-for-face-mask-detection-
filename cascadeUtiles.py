import os

# def generate_negative_description_file():
#     with open('neg.txt', 'w') as f:
#         for filename in os.listdir('negative'):
#             file_path = os.path.join('negative', filename)
#             f.write(file_path + '\n') 
          

# generate_negative_description_file()

import subprocess

command = 'D:/Newfolder/opencv/build/x64/vc14/bin/opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 2600 -vec pos.vec'

try:
    subprocess.run(command, shell=True, check=True)
    print("Command executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
