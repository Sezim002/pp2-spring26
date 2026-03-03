#1 
with open("sample.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")
#2
with open("sample.txt", "r") as f:
    print(f.read())
#3
with open("sample.txt", "a") as f:
    f.write("Line 4\n")
#4 
import os

if os.path.exists("backup_sample.txt"):
    os.remove("backup_sample.txt")
