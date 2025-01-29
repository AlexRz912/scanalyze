from helpers import projects_helper
from helpers import config_helper
from views import menu_view

def handle_menu():
    menu_view.display_start_menu()

def list_projects_into_action(path, action):
    projects_helpers.list_projects(path)
    return projects_helpers.select_project(action)

def handle_start_menu_choice(config_path, config_file, working_path, project_path):
    user_choice = input()
    if (user_choice == '2'):
        print("\n")
        project = list_projects_into_action(working_path, "load")
        print(f"{project} selected, configuring environment...")
        config_helpers.update_project_path(config_path, config_file, working_path, project)
        return False

    elif (user_choice == '3'):
        print("\n")
        list_projects_into_action(working_path, "delete")
        delete_flag = projects_helpers.delete_confirmation(project)
        projects_helpers.delete_project_on_confirmation(delete_flag, project)
        return True

    elif (user_choice == '4'):
        print("See ya !")
        return "bye"

    else:
        project = input("Choose a project name\n") 
        projects_helpers.new_project(project, working_path)
        config_helpers.update_project_path(config_path, config_file, working_path, project)
        return False