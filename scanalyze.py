import asyncio
from banner import display_banner
from controllers import menuController
from modules import modules

display_banner()

menuController.menu_controller("start")
#project_config = modules.handle_start_menu()

# asyncio.run(modules.handle_main_loop(project_config))

    
    # Verify if domain is filled
        # How to verify if it contains line? (not looking for wc -l output to terminal but to reuse it in a variable)
        # How to verify if those lines are related to domains? (regex I suppose)

    # If domains is filled, then we can display options_menu

        # As a user, I should be able to use any of the tools I want at any time with options and flags I provide

        # I should be able to automate whatever part I want and have control over the part that I want to do manually
        # data structures,  

        # I should be able to display the result anytime I want (program interruption/threading:low level mechanisms)

        # I should be able to sort the resuts I already have into different folders at ANY given moment (backgrounding, threading)

        # I should be able to come back to a specific step to add more stuff and 
        # decide to automatically or manually redo previous steps

        # I should be able to specify options manually from the config file

        # I should be able to configure options from the menus

        # I should be able to disable asking for options

        # I should be able to have one main step-by-step process
        # use multiple tools for each steps and also have the possibility to use tools outside the main step-by-step routine
    
    # modules.recon_module("automatic")
    # start_bug_hunt_routine(project_path, tooling, output_path, input_path)

