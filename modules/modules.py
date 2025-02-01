import asyncio
from modules.menu_modules.start_menu_module import start_menu_module
from modules.menu_modules.main_menu_module import main_menu_module
from modules.tool_modules import bug_hunt_routine

from handlers.submain_menu_handler import submain_menu_handler

from config.config_loader import *

def handle_start_menu():
    return start_menu_module(load_config("app"))
    # YAGNI principle again
    # elif (menu == "tool_mode_menu"):
        # main_menu_module.tool_mode_menu()

async def handle_main_loop():
    
    user_menu_choice = ""
    project_state = load_config("project")
    previous_recon = None
    previous_recon_exists = ""
    if not previous_recon:
        previous_recon_exists = False # problématique, vérifier le project_state depuis la project_config
    while (True):
        if user_menu_choice == "":
            user_menu_choice = main_menu_module()
        if not previous_recon_exists:
            previous_recon = await submain_menu_handler(user_menu_choice)
        break   

# def recon_module(mode):
    # config = load_config()
    # if (mode == "automatic"):
        # bug_hunt_routine.start_bug_hunt_routine(
            # )
