#1 
import os
os.makedirs("project/data/files", exist_ok=True)
#2
print(os.listdir("project"))
#3 
files = [f for f in os.listdir() if f.endswith(".txt")]
print(files)
#4
import shutil
shutil.move("sample.txt", "project/sample.txt")