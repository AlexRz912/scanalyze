import os
from banner import display_banner
import menu
import projects_handler

display_banner()



user_keeps_working = True

while (user_keeps_working):

    menu.display_project_menu()
    user_choice = input()

    if (user_choice == '2'):
        print("\n")
        # code to load project

        # debug if no project exist
        projects_handler.list_projects()
        project = projects_handler.choose_projects("load")
        print(f"{project} selected, configuring environment...")


        # prepare environment

    elif (user_choice == '3'):
        # code to delete project
        print("\n")
        projects_handler.list_projects()
        project = projects_handler.choose_projects("delete")
        delete_flag = projects_handler.delete_confirmation(project)
        projects_handler.delete_project_on_flag(delete_flag, project)

    elif (user_choice == '4'):
        print("\n")
        print("choose a path to your projects")
        
    elif (user_choice == '5'):
        print("See ya !")
        break
    else:
        print("1 is default choice")
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

    keep_working_flag = input("Continue working? (y/else)")
    if (keep_working_flag.lower() != "y"):
        user_keeps_working = False
