from utils.fileUtils import deleteUtil
from utils.fileUtils import createUtil
from utils.fileUtils import readUtil
from utils.fileUtils import printUtil
from utils.ioUtils import shExecUtil

def create_file(file):
    createUtil.create_file(file)

def create_folder(file):
    createUtil.create_folder(file)
    
def delete(file):
    deleteUtil.delete(file)

def read(file):
    file_content = readUtil.read(file)[0]
    return file_content

def print(file):
    printUtil.print(file)

def list_files_into_temp(path, file):
    shExecUtil.cmd_exec(f"ls {path}")