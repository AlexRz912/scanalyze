import time
from views import projectSortingViews
from handlers.menuHandlers import sortingActionHandlers

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
        sortingActionHandlers.sort_on_preset()
        return False
    elif (choice == "2"):
        sortingActionHandlers.custom_sort(path)
        return False
    elif (choice == "3"):
        sortingActionHandlers.display_specific_folder_tree(path)
        return False
    elif (choice == "4"):
        sortingActionHandlers.display_file_content(path)
        return False
    elif (choice == "5"):
        return True
    else:
        print("you've provided an non processed input, please provide a number according to this menu action")
        time.sleep(2)
        return False