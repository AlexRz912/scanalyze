from views import projectSortingViews
from handlers.menuHandlers import sortingActionHandlers

def sorting_menu_controller(path):
    projectSortingViews.display_project_tree(path)
    projectSortingViews.display_sorting_menu()
    choice = input()
    sorting_action(choice)


def sorting_action(choice):
    if (choice == "1"):
        sortingActionHandlers.sort_on_preset()
    elif (choice == "2"):
        sortingActionHandlers.custom_sort()
    elif (choice == "3"):
        sortingActionHandlers.display_specific_folder_tree()
    elif (choice == "4"):
        sortingActionHandlers.display_file_content()
    else:
        return choice