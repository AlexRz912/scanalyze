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
from helpers.domainFileHelpers import savePrevDomainFileHelpers

"""
This is no MVC as there is no Models in relation to Database but I use the word Controller
because it is the file that manages
all of the logic that starts from menu feature from, view
to specific action handlers
"""

def action_controller(menu, load_state=True):
    if (menu == "start"):
        startMenuView.display_start_menu()
        choice = input()
        return start_menu_action(choice)
    elif (menu == "main"):
        mainMenuView.display_main_menu()
        choice = input()
        return main_menu_action(choice, load_state)
    
def start_menu_action(action):
    project_path = None
    if (action == "1"):
        project_path = createProjectHandler.create()
        print("start menu creation calls load_config_for_state_handling with provided to false and project path")
        time.sleep(5)
        load_config_for_state_handling(False, project_path)
    elif (action == "2"):
        project_path = loadProjectHandler.load()
        load_config_for_state_handling(False, project_path)
    elif (action == "3"):
        deleteProjectHandler.delete()
    else:
        print("see ya")
        action = "quit"
    return action, project_path

def main_menu_action(action, load_state=True):
    if (action == "1"):
        config = configLoader.load_config("app")
        project_config = configLoader.load_config("project")

        domains_provided = recon_controller(config, project_config)
        load_config_for_state_handling(domains_provided)
    return action

def load_config_for_state_handling(provided, path=None):
    if path == None:
        print("-------------------------------------------")
        print("when there's no project path provided we're loading config")
        print("-------------------------------------------")
        time.sleep(10)
        config = configHelper.config_get("app", ["project_path"])
        path = config["project_path"]
    

    config = loadProjectHandler.project_config_path(path)
    project_config_path = configHelper.load_config_path("project", path)

    if not projectStateHandler.is_new_project(config):
        print("-----------------------------------------------")
        print("if project is not a new project we set previous_folder and domains_file")
        print("-----------------------------------------------")
        time.sleep(15)
        # in all case I do verify if it's not a new project
        previous_folder = (f"{path}/previous")
        domains_file = (f"{path}/domains")
    else:
        print("--------------------------------------------")
        print("project is a new project, therefore we don't need to verify if there are new domains provided")
        print("--------------------------------------------")
        time.sleep(15)
    projectStateHandler.set_state(project_config_path, path, config, provided)