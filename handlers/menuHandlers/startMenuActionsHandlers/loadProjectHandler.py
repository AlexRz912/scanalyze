from helpers.configHelper import config_get
from helpers.configHelper import update_project_path
from helpers.menuHelper import list_projects_into_action

from config import configLoader

def load():
    config = config_get(
            "app", 
            [
                "working_path",
                "project_path"
            ]
        )
    print("\n")
    project = list_projects_into_action(config["working_path"], "load")
    update_project_path(config["working_path"], project)

def project_config_path(path):
    return configLoader.load_config("project")

def update_config():
    return