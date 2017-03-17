import os

file_list = os.listdir(r"C:\Users\timur.minnakhmetov\Documents\udacity\New folder")
print file_list
os.chdir(r"C:\Users\timur.minnakhmetov\Documents\udacity\New folder")
for file_name in file_list:
    os.rename(file_name, file_name.translate(None, "012456789"))
