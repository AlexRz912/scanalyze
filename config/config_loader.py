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
        return

    