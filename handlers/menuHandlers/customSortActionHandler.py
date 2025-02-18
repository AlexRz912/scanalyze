from utils.fileUtils import lineNumUtil

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