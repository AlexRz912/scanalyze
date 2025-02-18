from utils.ioUtils import inputUtils
from helpers.sortingHelpers import tempFileHelpers

def check_folder_status_to_return_folder_path(num, temp_file):
    if num < 1:
        print("No folder found")
        return None
    elif num >= 2:
        folder_path = inputUtils.get_input("Two or more folders were found, please provide a complete path from projects folder :\n")
        return folder_path
    else:
        folder_path = tempFileHelpers.read(temp_file)
        return folder_path

def check_files_status(num):
    if num < 1:
        return None
    elif num >= 2:
        file = inputUtils.get_input("Two or more files were found, please provide a complete path from projects folder :\n")
        return file
    else:
        return "file_found_flag"