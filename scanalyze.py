import os
from banner import display_banner
import menu
import projects_handler
from config import config_handler

display_banner()

config_path = config_handler.load_config_path()
config_file = config_handler.load_config_file(config_path)

working_path = config_handler.set_working_path(config_file)
project_path = ""
# Code for loading working path


while (True):

    if (not config_handler.check_working_path_exists(working_path)):
            break
    menu.display_start_menu()
    user_choice = input()
    
    if (user_choice == '2'):
        print("\n")

        
        # code to load project
        # debug if no project exist
        projects_handler.list_projects(working_path)
        project = projects_handler.choose_projects("load")
        print(f"{project} selected, configuring environment...")
        project_path = config_handler.set_project_path(working_path, project)
        config_handler.update_project_path(config_path, config_file, project_path)
        # prepare environment

    elif (user_choice == '3'):
        # to refactor
        # code to delete project
        print("\n")
        projects_handler.list_projects(working_path)
        project = projects_handler.choose_projects("delete")
        delete_flag = projects_handler.delete_confirmation(project)
        projects_handler.delete_project_on_flag(delete_flag, project)
        
    elif (user_choice == '4'):
        print("See ya !")
        break
    else:
        print("create a new project")
        # code to create project

        # name project
        # create folder with name of project
        # prepare environment

    # menu.display_mode_menu()
    # it does reload the whole loop, without taking care of the imports
    # the following steps are hardcoded here and are not dynamically handled

    from tools import assetfinder
    from tools import httpx
    import save
    from tools import awk
    from tools import fff
    from tools import gf

