from helpers.configHelper import load_config_path
from helpers.configHelper import load_config_file
from helpers.configHelper import get_project_path
from helpers.configHelper import config_get

def load_config(config_type):
    if config_type == "app":
        return config_get(
            config_type,
            [ 
                "working_path",
                "project_path",
                "tool_routine",
                "output_path",
                "input_path"
            ]
        )
    elif config_type == "project":

        config_path = load_config_path("app")
        config_file = load_config_file(config_path)
        project_path = get_project_path(config_file)
        return config_get(
            config_type,
            [
                "project_name",
                "settings",
                "new_project",
                "recon"
            ],
            project_path
        )

    