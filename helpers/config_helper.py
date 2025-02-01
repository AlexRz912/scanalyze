import os
import json

def load_config_path(config_type, project_path=None):
    if (config_type == "app"):
        return os.path.join("config", "config.json")
    elif (config_type == "project"):
        return os.path.join(f"{project_path}/project_config/project_config.json")

def load_config_file(file_path):
    """Loads JSON from given file path"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file '{file_path}' not found")
    
    with open(file_path, 'r') as file:
        return json.load(file)

def get_project_path(config):
    return config.get("project_path")

def config_get(config_type, keys=[], project_path=None):
    config = {}
    config["config_path"] = load_config_path(config_type, project_path)
    config["config_file"] = load_config_file(config["config_path"])
    for i in keys:
        config[i] = config["config_file"].get(i)  
    return config

def set_project_path(path, input):
    return (f"{path}/{input}")

def check_working_path_exists(path):
    if (not os.path.isdir(path)): 
        print("No path was found, please provide a correct path value to working_path : config/config.json")
        return False
    return True
# def create_project_path(input):

def save_config(config_path, data):
    with open(config_path, 'w') as file:
        json.dump(data, file, indent=4)  # `indent=4` for readability

def update_project_path(config_path, config_file, working_path, project):
    path = set_project_path(working_path, project)
    # Update changes
    config_file["project_path"] = path
    
    # Save changes
    save_config(config_path, config_file)
    print(f"Project path successfully updated : {path}")


def init_project_config(data, project_path):
    os.system(f"mkdir {project_path}/project_config")
    os.system(f"touch {project_path}/project_config/project_config.json")

    
