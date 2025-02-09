import os
import json

def list_projects(working_path):
    if os.path.isdir(working_path):
        print("\033[93mAvailable projects\033[0m\n")
        for project in os.listdir(working_path):
            print(f"{project}")
        print("")
    else:
        print("No projects directory found.")

def select_project(action):
    return input(f"\033[96mSelect a project to {action} \33[0m\n\n")

def new_project(project_name, working_path):
    if os.path.isdir(working_path):
        os.system(f"mkdir {working_path}/{project_name}")
        os.system(f"mkdir {working_path}/{project_name}/previous")
        os.system(f"touch {working_path}/{project_name}/domains")
        os.system(f"touch {working_path}/{project_name}/previous/domains")
        os.system(f"mkdir {working_path}/{project_name}/project_config")
        os.system(f"touch {working_path}/{project_name}/project_config/project_config.json")
        
        config_path = (f"{working_path}/{project_name}/project_config/project_config.json")

        data = {
            "project_name": project_name,
            "settings": {
                "tutorial_mode": False,
                "suggestions_mode": False,
                "automatic_mode": False
            },
            "new_project": True,
            "pending_recon": False
            
        }

        with open(config_path, 'w') as file:
            json.dump(data, file, indent=4)
    else:
        print("No projects directory found.")

def delete_confirmation(choice):
    return input(f"\033[92mAre you sure to delete project : {choice} (y/else)\033[0m")
    
def delete_project_on_confirmation(delete_flag, choice):
    if (delete_flag == "y"):
        os.system(f"rm -rf ./projects/{choice}")
        return True
    return False