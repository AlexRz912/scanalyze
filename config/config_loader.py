from helpers import configHelper

def load_config(config_type):
    if config_type == "app":
        return configHelper.config_get(
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

        config_path = configHelper.load_config_path("app")
        config_file = configHelper.load_config_file(config_path)
        project_path = configHelper.get_project_path(config_file)
        print(project_path)
        return configHelper.config_get(
            config_type,
            [
                "",
                "",
                "",
                "",
                ""
            ],
            project_path
        )

    