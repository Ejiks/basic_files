import os

file_dic = {}
for file in os.listdir(os.getcwd()):
    if file.endswith(".txt") and file != "sum_files.txt":
        with open(file, "r", encoding="utf-8") as f:
            text = f.readlines()
            name = {file : text}
            file_dic[len(text)] = name

with open ("sum_files.txt", "w", encoding="utf-8") as f:
    for file_len in sorted(file_dic):
        atributes = file_dic.get(file_len)
        file_name = "".join(atributes.keys())
        f.write(file_name+"\n")
        f.write(str(file_len)+"\n")
        f.write("".join((atributes.get(file_name)))+"\n")

