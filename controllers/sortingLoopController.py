import time
from views import projectSortingViews

from handlers.menuHandlers import customSortActionHandler
from handlers.menuHandlers import displayFolderTreeHandler
from handlers.menuHandlers import displayFileHandler

from helpers.sortingHelpers import tempFileHelpers

from utils.ioUtils import inputUtils

def run_sorting_loop(path):
    while True:
        projectSortingViews.display_project_tree(path)
        projectSortingViews.display_sorting_menu()
        choice = input()
        user_quits_sorting = sorting_action(choice, path)
        if user_quits_sorting:
            break


def sorting_action(choice, path):
    if (choice == "1"):
        sort_on_preset()
        return False
    elif (choice == "2"):
        custom_sort(path)
        return False
    elif (choice == "3"):
        display_specific_folder_tree(path)
        return False
    elif (choice == "4"):
        display_file_content(path)
        return False
    elif (choice == "5"):
        return True
    else:
        print("you've provided an non processed input, please provide a number according to this menu action")
        time.sleep(2)
        return False


def sort_on_preset():
    print("sort_on_preset")


def custom_sort(path):

    sort_string = inputUtils.get_input("Choose a value to find: \n")
    sorting_results_folder = f"{sort_string}_results"
    customSortActionHandler.create_sorting_results_folder(path, sorting_results_folder)

    while True:
        folder_name = inputUtils.get_input("Choose a folder to work with: \n")
        
        folder = customSortActionHandler.find_folder(path, folder_name, sort_string)
        
        if folder:
            folder_path = tempFileHelpers.read(f"{path}/temp/found")
            folder_path = folder_path.strip()
            list_temp_file = tempFileHelpers.create_temp_folder(path, "list")

            tempFileHelpers.list_files_into_temp(folder_path, list_temp_file, sort_string)
            # get file corresponding lines, whole file or above directory? (l/f/a)
            # read_temp_into_copying_file
            # On trouve le fichier pour ensuite le copier dans notre fichier de résultat
            # tempFileHelpers.delete(f"{path}/temp")
            break
        else:
            tempFileHelpers.delete(f"{path}/temp")
            continue

def display_specific_folder_tree(path):
    while True:
        folder_name = inputUtils.get_input("Enter a folder name to display its specific tree :\n")
        done = displayFolderTreeHandler.find_folder_and_print_tree(path, folder_name)
        if not done:
            continue
        else:
            tempFileHelpers.delete(f"{path}/temp")
            break

def display_file_content(path):
    while True:
        file_name = inputUtils.get_input("Enter a file name to display its content :\n")
        done = displayFileHandler.find_files_and_print_content(path, file_name)
        if not done:
            continue
        else:
            tempFileHelpers.delete(f"{path}/temp")
            break
