from utils.fileUtils import deleteUtil
from utils.fileUtils import createUtil
from utils.fileUtils import readUtil
from utils.fileUtils import printUtil
from utils.ioUtils import shExecUtil

import time


def create_file(file):
    createUtil.create_file(file)

def create_folder(file):
    createUtil.create_folder(file)
    
def delete(file):
    deleteUtil.delete(file)

def read(file):
    file_content = readUtil.read(file)[0]
    return file_content

def cat(file):
    printUtil.print(file)

def list_files_into_temp(path, file, sort_string):  
    print(f"grep -rlw '{sort_string}' {path} | anew {file}")
    shExecUtil.cmd_exec(f"grep -rl '{sort_string}' {path} | anew {file}")
    # -rlE '\\200\\b' 

def create_temp_folder(path, temp_file):
    temp_path = f"{path}/temp/"
    
    create_folder(temp_path)
    create_file(f"{temp_path}{temp_file}")

    return f"{temp_path}{temp_file}"