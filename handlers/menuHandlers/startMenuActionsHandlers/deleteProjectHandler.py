from helpers.configHelper import config_get
from helpers.projectsHelper import delete_confirmation
from helpers.projectsHelper import delete_project_on_confirmation
from helpers.menuHelper import list_projects_into_action

def delete_project_handler():
    config = config_get(
            "app", 
            [
                "working_path",
                "project_path"
            ]
        )
    print("\n")
    project = list_projects_into_action(config["working_path"], "delete")
    delete_flag = delete_confirmation(project)
    delete_project_on_confirmation(delete_flag, project)
    