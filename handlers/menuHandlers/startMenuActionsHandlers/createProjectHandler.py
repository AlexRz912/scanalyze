from helpers.projectsHelper import new_project
from helpers.configHelper import config_get
from helpers.configHelper import update_project_path

def create_project_handler():
    config = config_get(
            "app", 
            [
                "working_path",
            ]
        )
    project = input("Choose a project name\n")
    new_project(project, config["working_path"])
    update_project_path(config["working_path"], project)