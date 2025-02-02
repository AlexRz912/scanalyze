from views import mainMenuView
from views import startMenuView
from handlers.menuHandlers.startMenuActionsHandlers.createProjectHandler import create_project_handler
from handlers.menuHandlers.startMenuActionsHandlers.loadProjectHandler import load_project_handler
from handlers.menuHandlers.startMenuActionsHandlers.deleteProjectHandler import delete_project_handler

"""
This is no MVC as there is no Models for Database but I use the word Controller
because it is the file that manages
all of the logic of the menu feature from the view
to specific action handlers
"""

def menu_controller(menu):
    if (menu == "start"):
        startMenuView.display_start_menu()
        choice = input()
        start_menu_action(choice)
    elif (menu == "main"):
        mainMenuViews.display_main_menu()
        choice = input()
        main_menu_action(choice)
    
def start_menu_action(action):
    if (action == "1"):
        create_project_handler()
    elif (action == "2"):
        load_project_handler()
    elif (action == "3"):
        delete_project_handler()
    else:
        print("see ya")
