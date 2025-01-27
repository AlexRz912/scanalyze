import os

def list_projects():
    projects_path = "./projects"  # Chemin vers le dossier à lister
    if os.path.isdir(projects_path):  # Vérifie que le chemin est un dossier
        print("Available projects:")
        print("\n")
        for project in os.listdir(projects_path):
            print(f"- {project}")
        print("\n")
    else:
        print("No projects directory found.")

def choose_projects(action):
    return input(f"Choose a project to {action} : ")

def delete_confirmation(choice):
    return input(f"Are you sure to delete project : {choice} (y/else)")

def delete_project_on_flag(delete_flag, choice):
    if (delete_flag == "y"):
        os.system(f"rm -rf ./projects/{choice}")

