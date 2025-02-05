import time
from views import startMenuView
from views import mainMenuView

from handlers.menuHandlers.startMenuActionsHandlers import createProjectHandler
from handlers.menuHandlers.startMenuActionsHandlers import loadProjectHandler
from handlers.menuHandlers.startMenuActionsHandlers import deleteProjectHandler

from handlers.projectStateHandlers import projectStateHandler

from .reconController import recon_controller

from config import configLoader
from helpers import configHelper

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
        load_config_for_state_handling(createProjectHandler.create())
        
    elif (action == "2"):
        load_config_for_state_handling(loadProjectHandler.load())
        
    elif (action == "3"):
        DeleteProjectHandler.delete()
    else:
        print("see ya")
        action = "quit"
    return action

def main_menu_action(action):
    if (action == "1"):
        config = configLoader.load_config("app")
        project_config = configLoader.load_config("project")
        print(project_config)
        time.sleep(100)
        recon_controller(config, project_config)
    return action

def load_config_for_state_handling(path=None, project=None):
    config = loadProjectHandler.project_config_path(path)
    project_config_path = configHelper.load_config_path("project", path)
    print(project_config_path)
    time.sleep(100)
    projectStateHandler.set_state(project_config_path, path, config)