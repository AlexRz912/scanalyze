from utils.ioUtils import outputUtils

def display_sorting_menu():
    print("sort by preset                      : press 1\n")
    print("custom sorting                      : press 2\n")
    print("display folder tree                 : press 3\n")
    print("display a file's content            : press 4\n")
    
def display_project_tree(project_path):
    outputUtils.tree_folders(project_path)

def display_specific_folder(path):
    outputUtils.tree_folders(path)

