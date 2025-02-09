import time
from views import startMenuView
from views import mainMenuView

from handlers.menuHandlers.startMenuActionsHandlers import createProjectHandler
from handlers.menuHandlers.startMenuActionsHandlers import loadProjectHandler
from handlers.menuHandlers.startMenuActionsHandlers import deleteProjectHandler

from handlers import domainFileHandler

from .reconController import recon_controller

from .projectStateController import *

from config import configLoader

from helpers import configHelper
from helpers.domainFileHelpers import savePrevDomainFileHelpers

"""
This is no MVC as there is no Models in relation to Database but I use the word Controller
because it is the file that manages all of the logic that starts from menu feature from, view
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
        project_path = createProjectHandler.create()
        conf, project_path, project_config_path = load_necessary_config()
        
    elif (action == "2"):

        loadProjectHandler.load()
        conf, project_path, project_config_path = load_necessary_config()
        conf["project_config"] = unset_new_on_existing_recon_result(project_path, project_config_path, conf["project_config"])
        set_pending_on_new_domains(conf["project_config"], project_config_path, project_path)
        
    elif (action == "3"):
        deleteProjectHandler.delete()

    else:
        print("see ya")
        action = "quit"
    return action

def main_menu_action(action):

    if (action == "1"):
        conf, project_path, project_config_path = load_necessary_config()
        set_pending_on_new_domains(conf["project_config"], project_config_path, project_path)
        recon_successful = recon_controller(project_path, conf["project_config"])
        
        update_project_vitals(

            project_config_path, 
            conf["project_config"], 
            f"{project_path}", 
            recon_successful

        )
    return action


def load_necessary_config():
    config = {}
    config["app_config"] = configLoader.load_config("app")
    config["project_config"] = configLoader.load_config("project")

    return config, config["app_config"]["project_path"], f"{config['app_config']['project_path']}/project_config/project_config.json"

def unset_new_on_existing_recon_result(path, project_config_path, project_config):
    if httpx_results_exist(f"{path}/httpx"):
        return state_unset_new(project_config_path, project_config)
    return project_config

def set_pending_on_new_domains(project_config, project_config_path, project_path):
    different = domainFileHandler.domain_file_has_changed(project_path)
    state_set_pending(project_config_path, project_config, different)

def update_project_vitals(project_config_path, project_config, path, success):
    update_prev_domains_file(success, path)
    project_config = unset_new_on_existing_recon_result(path, project_config_path, project_config)
    state_unset_pending(project_config_path, project_config, success)

def update_prev_domains_file(success, path):
    print(path)
    if success:
        savePrevDomainFileHelpers.save(f"{path}/domains", path)