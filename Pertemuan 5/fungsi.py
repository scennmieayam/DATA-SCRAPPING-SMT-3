import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

def write_to_file(path, data):
    with open(path,'a') as file:
        file.write(data + '\n')