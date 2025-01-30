from modules.menu_modules import main_menu_module
from modules.tool_modules import bug_hunt_routine
from config.config_loader import *

def handle_menus(menu):
    if (menu == "start_menu"):
        main_menu_module.main_menu(load_config())
    # YAGNI principle again
    # elif (menu == "tool_mode_menu"):
        # main_menu_module.tool_mode_menu()

def recon_module(mode):
    config = load_config()
    if (mode == "routine"):
        bug_hunt_routine.start_bug_hunt_routine(
            config["project_path"], 
            config["tooling"], 
            config["output_path"], 
            config["input_path"])
