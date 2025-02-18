from helpers.sortingHelpers import findFileHelper
from helpers.sortingHelpers import tempFileHelpers
from helpers.sortingHelpers import checkStatusHelper
from utils.fileUtils import lineNumUtil
from utils.ioUtils import outputUtils
from utils.ioUtils import inputUtils

def find_folder_and_print_tree(path, folder):
    
    found_temp_file = tempFileHelpers.create_temp_folder(path, "found")
    findFileHelper.find_folder_to_print(path, folder, found_temp_file)
    line_num = lineNumUtil.get_line_num(found_temp_file)

    folder_found = checkStatusHelper.check_folder_status_to_return_folder_path(line_num, found_temp_file)

    if folder_found:
        outputUtils.tree_folders(folder_found)
        inputUtils.get_input("\n\npress enter to continue")
        return True
    return False