import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

def write_to_file(path, data):
    with open(path,'a') as file:
        file.write(data + '\n')

def read_data(path):
    with open(path,'rt') as file:
        for line in file:
            print(line.replace("\n",""))
            