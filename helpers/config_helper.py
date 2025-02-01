import os
import json

def load_config_path(config_type):
    if (config_type == "app"):
        return os.path.join("config", "config.json")
    elif (config == "project"):
        return 

def load_config_file(config_path):
    """Loads JSON from given file path"""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file '{config_path}' not found")
    
    with open(config_path, 'r') as file:
        return json.load(file)

def config_get(config_type, keys=[]):
    config = {}
    config["config_path"] = load_config_path(config_type)
    config["config_file"] = load_config_file(config["config_path"])
    for i in keys:
        config[i] = config["config_file"].get(i)  # Ajoute la valeur de la clé i dans le dictionnaire config
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