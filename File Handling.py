#Python provides built in function and methods to read and write files.

#Read a whole file
with open('example.txt','r') as file:
    content=file.read();
    print(content)

#Read a file line by line
with open('example.txt','r') as file:
    for line in file:
        print(line.strip())   # .strip() remove spaces, newline spaces

#Writing a file(overwriting)
with open('example.txt','w') as file:
    file.write('Hi!\n')
    file.write('who are you?\n')

#writing file without overriding
with open('example.txt','a') as file:
    file.write('append new line1\n')
    file.write('append new line2\n')

#writing a list of lines to a file
line=['first line\n','second line\n', 'third line\n']
with open('example.txt','a') as file:
    file.writelines(line)

#Binary file

data=b'\x00\x01\x02\x03\x04'
with open('example2.bin','wb') as file:
    file.write(data)

#read content from source text file and write to a destination text file
with open('source.txt','r') as file:
    content=file.read()

with open('destination.txt','w') as file:
    file.write(content)

#read text file and count the number of lines, words, and characters
def count_text_file(file_path):
    with open(file_path,'r') as files:
        lines=files.readlines()
        lines_count=len(lines)
        word_count=sum(len(line.split()) for line in lines)
        char_count=sum(len(line) for line in lines)
    return lines_count, word_count, char_count
file_path='example.txt'
lines,words,characters=count_text_file(file_path)
print(f'Total lines is {lines},total words is {words} and total characters is {characters}')

#Writing and then Reading file
with open('example.txt','w+') as file:       #The w+ mode in python for reading and writing file
    file.write('My name is pyhon\n')
    file.write('whats your name\n')
    file.seek(0)      #move the file cursor to the begning
    file.read()

#working with file paths

#creating a new directory
import os
new_directory='package'
#os.mkdir(new_directory)
print(f'new directory {new_directory} created')

#listing files and directories
items=os.listdir('.')
print(items)

#joining paths
dir_name='folder'
file_name='file.txt'
full_path=os.path.join(dir_name, file_name)
print(full_path)

#checking if the file or directory
path='example4.txt'
if os.path.exists(path):
    print(f'the path exists')
else:
    print(f'path not exists')

path1='example.txt'
if os.path.isfile(path1):
    print('file exists');
elif os.path.isdir(path1):
    print('directory exits')
else:
    print('neither a file nor a directory exists')

#Getting a absolute path
relative_path='example.txt'
absolute_path=os.path.abspath(relative_path)
print(absolute_path)