
file_path = './pi_digits.txt'

with open(file_path, 'w') as file_object:  # overwrite current content
    file_object.write("i love pi")


with open(file_path, 'a') as file_object:  # append new content
    file_object.write(" and i love math")


with open(file_path, 'r') as file_object:
    # contents = file_object.read()  # reads content of file char by char
    lines = file_object.readlines()  # reads content line by line

for line in lines:
    line = line.replace('i', 'I')
    print(line.rstrip())  # rstrip() method removes white spaces