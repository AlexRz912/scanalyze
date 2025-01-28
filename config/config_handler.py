import os
import json

def load_config_path():
    return os.path.join("config", "config.json")

def load_config_file(config_path):
    """Charge le fichier JSON à partir du chemin donné."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Le fichier de configuration '{config_path}' est introuvable.")
    
    with open(config_path, 'r') as file:
        return json.load(file)

def set_working_path(config_file):
    return config_file.get("working_path")

def check_working_path_exists(path):
    if (not os.path.isdir(path)): 
        print("No path was found, please provide a correct path value to working_path : config/config.json")
        return False
    return True

# def create_project_path(input):


def get_project_path(path, input):
    return (f"{path}/{input}")

def save_config(config_path, data):
    with open(config_path, 'w') as file:
        json.dump(data, file, indent=4)  # `indent=4` for readability


def update_project_path(config_path, config_file, path):
    
    # Update changes
    config_file["project_path"] = path
    
    # Save changes
    save_config(config_path, config_file)
    print(f"Project path successfully updated : {path}")