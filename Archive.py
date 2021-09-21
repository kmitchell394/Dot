import shutil
import os
import glob
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

source = r"D:\Dot\Dot EDI\\"
destination = r"D:\Dot\Dot EDI\OLD\\"


for f in files(r"D:\Dot\Dot EDI\\"):
	shutil.move(source + f, destination + f)

print("files moved")