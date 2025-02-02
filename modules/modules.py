import asyncio
from modules.menu_modules.start_menu_module import start_menu_module
from modules.menu_modules.main_menu_module import main_menu_module
from modules.tool_modules import bug_hunt_routine

from handlers.submain_menu_handler import submain_menu_handler

from config.config_loader import *

def handle_start_menu():
    while (True):
        choice = start_menu_module(load_config("app"))
        if (choice == "3"):
            continue
        return load_config("project")

async def handle_main_loop(project_config):
    while (True):
        user_menu_choice = main_menu_module()
        await submain_menu_handler(user_menu_choice)
        break   

# def recon_module(mode):
    # config = load_config()
    # if (mode == "automatic"):
        # bug_hunt_routine.start_bug_hunt_routine(
            # )
