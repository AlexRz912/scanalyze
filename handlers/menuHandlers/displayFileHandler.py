from utils.fileUtils import lineNumUtil
from utils.ioUtils import inputUtils

from helpers.sortingHelpers import tempFileHelpers
from helpers.sortingHelpers import findFileHelper
from helpers.sortingHelpers import checkStatusHelper

def find_files_and_print_content(path, file):
    found_temp_file = tempFileHelpers.create_temp_folder(path, "found")
    findFileHelper.find_and_print_to_temp(path, file, found_temp_file)
    line_num = lineNumUtil.get_line_num(found_temp_file)

    file_status_or_file = checkStatusHelper.check_files_status(line_num)
    
    if file_status_or_file == "file_found_flag":
        file_to_print = tempFileHelpers.read(found_temp_file)
        tempFileHelpers.cat(file_to_print)
        inputUtils.get_input("\n\npress enter to continue")

    elif file_status_or_file:
        tempFileHelpers.cat(file_status_or_file)
        inputUtils.get_input("\n\npress enter to continue")
    else:
        file_status_or_file = None

    return file_status_or_file