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

def set_project_path(path, input):
    return (f"{path}/{input}")

def save_config(config_path, data):
    """Écrit les modifications dans le fichier JSON."""
    with open(config_path, 'w') as file:
        json.dump(data, file, indent=4)  # `indent=4` pour une meilleure lisibilité

# Modifier une clé dans la configuration
def update_project_path(config_path, config_file, path):
    
    # Modifier la clé
    config_file["project_path"] = path
    
    # Sauvegarder les changements
    save_config(config_path, config_file)
    print(f"Le chemin de travail a été mis à jour avec succès : {path}")