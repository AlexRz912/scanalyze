import time
import os

from utils.fileUtils import lineNumUtil
from utils.fileUtils import filepathUtil
from utils.fileUtils import copyUtils
from utils.ioUtils import inputUtils

from helpers.sortingHelpers import findFileHelper
from helpers.sortingHelpers import tempFileHelpers
from helpers.sortingHelpers import checkStatusHelper

def find_folder(path, folder, sort_string):
    line_num, temp_file = get_printed_line_num_from_temp_file(path, folder, "found")
    folder_found = checkStatusHelper.check_folder_status_to_return_folder_path(line_num, temp_file)

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

    return f"{temp_path}{temp_file}"

def get_printed_line_num_from_temp_file(path, folder, name):
    found_temp_file = create_temp_folder(path, name)
    findFileHelper.find_folder_to_print(path, folder, found_temp_file)
    return lineNumUtil.get_line_num(found_temp_file), found_temp_file

def process_sorting_scope_choice(choice, list_temp_file, project_path, results_folder):
    file_content = tempFileHelpers.read_entire_file(list_temp_file)

    if choice == "l":
        sort_on_line_sorting_scope(project_path, file_content, results_folder)
    elif choice == "f":
        sort_on_file_sorting_scope(project_path, file_content, results_folder)
    elif choice == "d":
        sort_on_folder_sorting_scope(project_path, file_content, results_folder)

def sort_on_folder_sorting_scope(project_path, content, folder):
    directories = []
    for i in content:
        curr_dir = retrieve_current_directory(i)
        copy_folder_into_results_folder(curr_dir, project_path, folder)

def sort_on_file_sorting_scope(project_path, content, folder):
    for i in content:
        copy_file_into_results_folder(i, project_path, folder)
    

def sort_on_line_sorting_scope(project_path, content, sort_string, folder):
    paths = find_files_path_from_content_list(project_path, content)
    print(paths)
    time.sleep(3)
    return

def get_sorting_scope():
    while True:
        sorting_scope_choice = ask_for_sorting_scope()
        if sorting_scope_choice in ("l", "f", "d"):
            return sorting_scope_choice
        else:
            print("You've provided a non processed input, please reply with l, f or d\n")
            continue
    
def ask_for_sorting_scope():
    return inputUtils.get_input("get file corresponding lines, whole file or above directory? (l/f/d)\n")
    
def retrieve_current_directory(file_path):
    return filepathUtil.get_current_dir(file_path)

def copy_folder_into_results_folder(curr_dir, project_path, folder):
    copyUtils.copy_directory_into_folder(curr_dir, project_path, folder)

def copy_file_into_results_folder(file, project_path, folder):
    copyUtils.copy_file_into_folder(file, project_path, folder)