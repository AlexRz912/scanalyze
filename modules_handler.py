import projects_handler
from config import config_handler

def display_start_menu():
    print("\n\n")
    print("1: create new hunting project         : press 1\n")
    print("2: load hunting project               : press 2\n")
    print("3: delete hunting project             : press 3\n")
    print("4: to quit                            : press 4\n")
    

def display_mode_menu():
    print("1: for automatic mode      : press 1\n")
    print("2: for manual mode         : press 2\n")
    print("3: for customization       : press 3\n")
    print("4: to quit                 : press 4")

def list_projects_into_action(path, action):
    projects_handler.list_projects(path)
    return projects_handler.select_project(action)

def handle_start_menu_choice(config_path, config_file, working_path, project_path):
    user_choice = input()
    if (user_choice == '2'):
        print("\n")
        project = list_projects_into_action(working_path, "load")
        print(f"{project} selected, configuring environment...")
        config_handler.update_project_path(config_path, config_file, working_path, project)
        return False

    elif (user_choice == '3'):
        print("\n")
        list_projects_into_action(working_path, "delete")
        delete_flag = projects_handler.delete_confirmation(project)
        projects_handler.delete_project_on_confirmation(delete_flag, project)
        return True

    elif (user_choice == '4'):
        print("See ya !")
        return "bye"

    else:
        project = input("Choose a project name\n") 
        projects_handler.new_project(project, working_path)
        config_handler.update_project_path(config_path, config_file, working_path, project)
        return False