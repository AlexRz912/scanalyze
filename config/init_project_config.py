import os
import json

def init_project_config(data):
    os.system("mkdir project_config")
    os.system("touch project_config/project_config.json")

    config_path = "project_config/project_config.json"
    with open(config_path, 'w') as file:
        json.dump(data, file, indent=4)

data = {
    "project_name": "My Project",
    "version": "1.0",
    "dependencies": ["library1", "library2"],
    "settings": {
        "debug": True,
        "max_users": 100
    }
}
init_project_config(data)
