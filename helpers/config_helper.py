import os
import json

def load_config_path():
    return os.path.join("config", "config.json")

def load_config_file(config_path):
    """Loads JSON from given file path"""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file '{config_path}' not found")
    
    with open(config_path, 'r') as file:
        return json.load(file)

def get_working_path(config_file):
    return config_file.get("working_path")

def get_project_path(config_file):
    return config_file.get("project_path")
    
def get_tooling(config_file):
    return config_file.get("tool_routine")

def get_tool_input_path(config_file):
    return config_file.get("tool_input_path")

def get_tool_output_path(config_file):
    return config_file.get("tool_output_path")

def config_get(config_file, key):
    return config_file.get(key)

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