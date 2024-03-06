import os
import shutil

img_ext = [".jpg", ".png"]


def is_dir(path):
    if not os.path.isdir(path):
        raise Exception(f"Dir {path} not found")


try:
    is_dir(path_src := input("Enter path to src: "))
    is_dir(path_dst := input("Enter path to dst: "))
except Exception as inst:
    exit(inst)

for curr_dir, _, files in os.walk(path_src):
    for file in files:
        file_path = os.path.join(curr_dir, file)
        if os.path.splitext(file_path)[1] in img_ext:
            # TODO use move instead of copy
            shutil.copy(file_path, path_dst)
            # print(file)

print(shutil.make_archive("python_archive", "zip", "dst"))
