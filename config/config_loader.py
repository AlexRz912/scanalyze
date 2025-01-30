from helpers import config_helper

def load_config():
    config = {}
    config["config_path"] = config_helper.load_config_path()
    config["config_file"] = config_helper.load_config_file(config["config_path"])
    config["working_path"] = config_helper.get_working_path(config["config_file"])
    config["project_path"] = config_helper.get_project_path(config["config_file"])
    config["tooling"] = config_helper.get_tooling(config["config_file"])
    config["output_path"] = config_helper.get_tool_output_path(config["config_file"])
    config["input_path"] = config_helper.get_tool_input_path(config["config_file"])
    return config