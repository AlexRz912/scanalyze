from helpers import config_helper

def load_config(config_type):
    if config_type == "app":
        return config_helper.config_get(
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

        config_path = config_helper.load_config_path("app")
        config_file = config_helper.load_config_file(config_path)
        project_path = config_helper.get_project_path(config_file)
        print(project_path)
        return config_helper.config_get(
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

    