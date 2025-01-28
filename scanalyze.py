import os
from banner import display_banner
import menu
import projects_handler
from config import config_handler
from bug_hunt_routine import start_bug_hunt_routine

display_banner()

# externalise the handling of these for more code flexibility in the future
# lots of code have to be written inside this scanalyze file because of this
# one handler should have access to these and redistribute it to other .py
# project is not in refacto phase so I don't mind working with this for now

config_path = config_handler.load_config_path()
config_file = config_handler.load_config_file(config_path)

working_path = config_handler.get_working_path(config_file)
project_path = config_handler.get_project_path(config_file)
tooling = config_handler.get_tooling(config_file)

output_path = config_handler.get_tool_output_path(config_file)
input_path = config_handler.get_tool_input_path(config_file)

while (True):

    # Check line 10: These would be called inside a function from another file that takes config_path, config_file, 
    # working_path and project_path from a handler or whatever it should be called from a file architecture POV
    if (not config_handler.check_working_path_exists(working_path)):
        break
    menu.display_start_menu()
    user_choice = input()
    
    if (user_choice == '2'):
        print("\n")
        projects_handler.list_projects(working_path)
        project = projects_handler.choose_projects("load")
        print(f"{project} selected, configuring environment...")
        project_path = projects_handler.get_project_path(working_path, project)
        config_handler.update_project_path(config_path, config_file, project_path)

    elif (user_choice == '3'):
        print("\n")
        projects_handler.list_projects(working_path)
        project = projects_handler.choose_projects("delete")
        delete_flag = projects_handler.delete_confirmation(project)
        projects_handler.delete_project_on_flag(delete_flag, project)
        continue

    elif (user_choice == '4'):
        print("See ya !")
        break

    else:
        project = input("Choose a project name\n") 
        projects_handler.new_project(project, working_path)
        project_path = projects_handler.get_project_path(working_path, project)
        config_handler.update_project_path(config_path, config_file, project_path)

    start_bug_hunt_routine(project_path, tooling, output_path, input_path)
    # YAGNI principle :D
    # menu.display_mode_menu()

    # from tools import assetfinder
    # from tools import httpx
    # import save
    # from tools import awk
    # from tools import fff
    # from tools import gf

