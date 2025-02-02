from . import projects_helper
from . import config_helper

def list_projects_into_action(path, action):
    projects_helper.list_projects(path)
    return projects_helper.select_project(action)

def handle_start_menu_choice(config_path, config_file, working_path, project_path):
    user_choice = input()
    if (user_choice == '2'):
        print("\n")
        project = list_projects_into_action(working_path, "load")
        print(f"{project} selected, configuring environment...")
        config_helper.update_project_path(config_path, config_file, working_path, project)

    elif (user_choice == '3'):
        print("\n")
        project = list_projects_into_action(working_path, "delete")
        delete_flag = projects_helper.delete_confirmation(project)
        projects_helper.delete_project_on_confirmation(delete_flag, project)
        
        
    elif (user_choice == '4'):
        print("See ya !")
        return "bye"

    else:
        project = input("Choose a project name\n") 
        projects_helper.new_project(project, working_path)
        config_helper.update_project_path(config_path, config_file, working_path, project)

    return user_choice

def handle_menu_choice(menu_type):
    return