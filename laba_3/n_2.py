import os
import shutil

zipExt = [x[0] for x in shutil.get_archive_formats()] 
print(zipExt)

path = input("Enter directory paht: ")
if not os.path.isfile(path):
    exit("Non valid path")

try:
    shutil.unpack_archive(path, './temp')
except ValueError:
    exit("Non valid file extension")

size = 0
for curr_dir, _, files in os.walk('./temp'):
    for file in files:
        file_path = os.path.join(curr_dir, file)
        size += os.path.getsize(file_path)
print(size)

shutil.rmtree('./temp')
