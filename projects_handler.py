import os

def get_project_path(path, input):
    return (f"{path}/{input}")

def list_projects(working_path):
    if os.path.isdir(working_path):  # Vérifie que le chemin est un dossier
        print("Available projects:")
        print("\n")
        for project in os.listdir(working_path):
            print(f"- {project}")
        print("\n")
    else:
        print("No projects directory found.")

def choose_projects(action):
    return input(f"Choose a project to {action} : ")

def new_project(project_name, working_path):
    if os.path.isdir(working_path):
        os.system(f"mkdir {working_path}/{project_name}")
    else:
        print("No projects directory found.")

def delete_confirmation(choice):
    return input(f"Are you sure to delete project : {choice} (y/else)")

def delete_project_on_flag(delete_flag, choice):
    if (delete_flag == "y"):
        os.system(f"rm -rf ./projects/{choice}")
        return True
    return False