import os

# path = r"C:\Users\user\Downloads\OST_문명6"
path = r"C:\Users\user\Downloads"
for old_name in os.listdir(path):
    new_name = old_name.replace("y2mate.com - ", "")
    os.rename(os.path.join(path, old_name), os.path.join(path, new_name))
    if old_name != new_name:
        print(f"{old_name:<100} -> {new_name:<100}으로 이름 변경")
