import os

root_path = r"C:\Users\user\Documents\Python_Summary"
target_path = "1_ 파이썬 기본"
file_path = os.path.join(root_path, target_path)
for file_1 in os.listdir(file_path)[1:]:
    file1_path = os.listdir(os.path.join(file_path, file_1))
    for file_2 in file1_path:
        old = os.path.join(os.path.join(file_path, file_1), file_2)
        new = os.path.join(os.path.join(file_path, file_1), file_2[4:])
        os.rename(old, new)

