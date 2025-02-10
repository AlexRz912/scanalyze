import time

from utils.ioUtils import inputUtils
from utils.ioUtils import outputUtils
from utils.fileUtils import lineNumUtil
from utils.fileUtils import deleteUtil
from utils.fileUtils import createUtil
from utils.fileUtils import readUtil
from utils.fileUtils import printUtil
from helpers.sortingHelpers import findFileHelper

def sort_on_preset():
    print("sort_on_preset")
    # display preset list

def custom_sort():
    print("custom_sort")

def display_specific_folder_tree():
    print("display_specific_folder_tree")
    
def display_file_content(path):
    while True:
        file_name = inputUtils.get_input("Enter the file name to display its content :\n")
        status = find_files_and_print_content(path, file_name)
        if not status:
            continue
        else:
            break
            
    # find "./project_path" -type f -name "nom_du_fichier.ext"
    
def find_files_and_print_content(path, file):
    temp_file = f"{path}/temp"

    create_temp_file(temp_file)
    findFileHelper.find_and_print_to_temp(path, file)

    line_num = lineNumUtil.get_line_num(temp_file)
    file_status_or_file = check_files_status(line_num)
    
    if file_status_or_file == "file_found_flag":
        file_to_print = read_temp_file(temp_file)
        print(file_to_print)
        time.sleep(4)
        print_file(file_to_print)
        delete_temp_file(temp_file)

    elif file_status_or_file:
        print_file(file_status_or_file)
        delete_temp_file(temp_file)
    else:
        file_status_or_file = None
        delete_temp_file(temp_file)
        
    
    return file_status_or_file

    # verifier le nombre de lignes du fichier temporaire
def check_files_status(num):
    if num < 1:
        print("No file found")
        return None
    elif num >= 2:
        file = inputUtils.get_input("Two or more files were found, please provide a complete path from projects folder :\n")
        return file
    else:
        print("displaying file")
        return "file_found_flag"

def create_temp_file(file_to_create):
    createUtil.create_file(file_to_create)

def delete_temp_file(file_to_delete):
    deleteUtil.delete(file_to_delete)

def read_temp_file(file_to_read):
    return readUtil.read(file_to_read)

def print_file(file_to_print):
    printUtil.print(file_to_print)