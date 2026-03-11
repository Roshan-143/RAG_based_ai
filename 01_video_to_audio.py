# import whisper  
import os
import subprocess
files=os.listdir("videos")
# print(files)
for file in files:
    # print(file)
    tut_number=file.split(" [")[0].split(" #")[1]
    file_names=file.split(" ｜ ")[0]
    # print(tut_number,file_names)
    subprocess.run(["ffmpeg","-i",f"videos/{file}",f"audios/{tut_number}_{file_names}.mp3"])