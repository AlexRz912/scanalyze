import time

from utils.ioUtils import inputUtils
from utils.ioUtils import outputUtils
from utils.fileUtils import lineNumUtil

from helpers.sortingHelpers import findFileHelper
from helpers.sortingHelpers import tempFileHelpers
from helpers.sortingHelpers import checkStatus

def sort_on_preset():
    print("sort_on_preset")

def custom_sort(path):

    sort_string = inputUtils.get_input("Choose a value to find: \n")
    sorting_results_folder = f"{sort_string}_results"
    create_sorting_results_folder(path, sorting_results_folder)

    while True:
        folder_name = inputUtils.get_input("Choose a folder to work with: \n")
        
        folder = find_folder(path, folder_name, sort_string)
        
        if folder:
            folder_path = tempFileHelpers.read(f"{path}/temp/found")
            list_temp_file = create_temp_folder(path, "list")
            tempFileHelpers.list_files_into_temp(folder_path, list_temp_file)
            tempFileHelpers.delete(f"{path}/temp")
            break
        else:
            tempFileHelpers.delete(f"{path}/temp")
            continue
            
    
def find_folder(path, folder, sort_string):

    line_num, temp_file = get_printed_line_num_from_temp_file(path, folder, "found")

    folder_found = checkStatus.check_folder_status_to_return_folder_path(line_num, temp_file)

    if folder_found:
        return folder 
    return False

def create_sorting_results_folder(path, results_folder):
    folder = f'{path}/{results_folder}'
    tempFileHelpers.create_folder(folder)

def create_temp_folder(path, temp_file):
    temp_path = f"{path}/temp/"
    
    tempFileHelpers.create_folder(temp_path)
    tempFileHelpers.create_file(f"{temp_path}{temp_file}")

    return f"{temp_path}/{temp_file}"

def get_printed_line_num_from_temp_file(path, folder, name):
    found_temp_file = create_temp_folder(path, name)
    findFileHelper.find_folder_to_print(path, folder, found_temp_file)
    return lineNumUtil.get_line_num(found_temp_file), found_temp_file

def display_specific_folder_tree(path):
    while True:
        folder_name = inputUtils.get_input("Enter a folder name to display its specific tree :\n")
        done = find_folder_and_print_tree(path, folder_name)
        if not done:
            continue
        else:
            tempFileHelpers.delete(f"{path}/temp")
            break
    
def display_file_content(path):
    while True:
        file_name = inputUtils.get_input("Enter a file name to display its content :\n")
        done = find_files_and_print_content(path, file_name)
        if not done:
            continue
        else:
            tempFileHelpers.delete(f"{path}/temp")
            break

def find_folder_and_print_tree(path, folder):
    
    found_temp_file = create_temp_folder(path, "found")
    findFileHelper.find_folder_to_print(path, folder, found_temp_file)
    line_num = lineNumUtil.get_line_num(found_temp_file)

    folder_found = checkStatus.check_folder_status_to_return_folder_path(line_num, found_temp_file)

    if folder_found:
        outputUtils.tree_folders(folder_found)
        inputUtils.get_input("\n\npress enter to continue")
        return True
    return False

def find_files_and_print_content(path, file):
    found_temp_file = create_temp_folder(path, "found")
    findFileHelper.find_and_print_to_temp(path, file, found_temp_file)
    line_num = lineNumUtil.get_line_num(found_temp_file)

    file_status_or_file = checkStatus.check_files_status(line_num)
    
    if file_status_or_file == "file_found_flag":
        file_to_print = tempFileHelpers.read(found_temp_file)
        tempFileHelpers.print(file_to_print)
        inputUtils.get_input("\n\npress enter to continue")

    elif file_status_or_file:
        tempFileHelpers.print(file_status_or_file)
        inputUtils.get_input("\n\npress enter to continue")
    else:
        file_status_or_file = None

    return file_status_or_file