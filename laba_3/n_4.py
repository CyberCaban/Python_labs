import collections
import os
from pprint import pprint

def is_dir(path):
    if not os.path.isdir(path):
        raise Exception(f"Dir {path} not found")


try:
    is_dir(src := input("Enter path to src: "))
except Exception as inst:
    exit(inst)

imps = collections.defaultdict(set) # {key(lib): [values(modules)]}

for curr_dir, _, files in os.walk(src):
    for file in files:
        file_path = os.path.join(curr_dir, file)
        if os.path.splitext(file_path)[1] == ".py":
            print(file_path)
            with open(file_path, "r") as f:
                lines = f.readlines()
            for line in lines:
                if "import" in (line := line.split()):
                    print(line)
                    import_index = line.index("import")
                    try:
                        from_index = line.index("from")
                        for module in line[import_index+1:]:
                            imps[line[from_index+1]].add(module.replace(",", ""))
                    except ValueError:
                        imps[line[import_index+1]]

with open("imports.py", "w") as f:
    f.truncate(0)
    for key, values in imps.items():
        if not str(key).isidentifier():
            continue
        if values == set():
            f.write(f"import {key}\n")
        else:
            f.write(f"from {key} import {', '.join(list(values))}\n")
pprint(imps)
        