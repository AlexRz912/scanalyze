from views import startMenuView
from views import mainMenuView
from handlers.menuHandlers.startMenuActionsHandlers.createProjectHandler import create_project_handler
from handlers.menuHandlers.startMenuActionsHandlers.loadProjectHandler import load_project_handler
from handlers.menuHandlers.startMenuActionsHandlers.deleteProjectHandler import delete_project_handler

from .reconController import recon_controller

"""
This is no MVC as there is no Models in relation to Database but I use the word Controller
because it is the file that manages
all of the logic that starts from menu feature from, view
to specific action handlers
"""

def action_controller(menu):
    if (menu == "start"):
        startMenuView.display_start_menu()
        choice = input()
        return start_menu_action(choice)
    elif (menu == "main"):
        mainMenuView.display_main_menu()
        choice = input()
        return main_menu_action(choice)
    
def start_menu_action(action):
    if (action == "1"):
        create_project_handler()
    elif (action == "2"):
        load_project_handler()
    elif (action == "3"):
        delete_project_handler()
    else:
        print("see ya")
        action = "quit"
    return action

def main_menu_action(action):
    if (action == "1"):
        recon_controller()