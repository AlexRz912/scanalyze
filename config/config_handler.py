import os
import json

def set_working_path():
    config_file = os.path.join("config", "config.json")

    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Config file '{config_path}' not found.")

    with open(config_file, 'r') as file:
        config = json.load(file)

    return config.get("working_path")

def check_working_path_exists(path):
    if (not os.path.isdir(path)): 
        print("No path was found, please provide a correct path value to working_path : config/config.json")
        return False
    return True
