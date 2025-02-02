from . import projectsHelper
# from . import configHelper

def list_projects_into_action(path, action):
    projectsHelper.list_projects(path)
    return projectsHelper.select_project(action)

# def handle_start_menu_choice(config_path, config_file, working_path, project_path):
    # user_choice = input()
    # if (user_choice == '2'):
        # return
# 
    # elif (user_choice == '3'):
        # print("\n")
        # project = list_projects_into_action(working_path, "delete")
        # delete_flag = projectsHelper.delete_confirmation(project)
        # projectsHelper.delete_project_on_confirmation(delete_flag, project)
        # 
        # 
    # elif (user_choice == '4'):
        # print("See ya !")
        # return "bye"
# 
    # else:
        # project = input("Choose a project name\n") 
        # projectsHelper.new_project(project, working_path)
        # configHelper.update_project_path(config_path, config_file, working_path, project)
# 
    # return user_choice
# 
# def handle_menu_choice(menu_type):
    # return