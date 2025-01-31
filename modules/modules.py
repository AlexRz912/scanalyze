import asyncio
from modules.menu_modules.start_menu_module import start_menu_module
from modules.menu_modules.main_menu_module import main_menu_module
from modules.tool_modules import bug_hunt_routine

from handlers.submain_menu_handler import submain_menu_handler

from config.config_loader import *

def handle_start_menu():
    start_menu_module(load_config())
    # YAGNI principle again
    # elif (menu == "tool_mode_menu"):
        # main_menu_module.tool_mode_menu()

async def handle_main_loop():
    user_menu_choice = ""
    recon_done = False
    while (True):
        if user_menu_choice == "":
            user_menu_choice = main_menu_module()
        if not recon_done:
            recon_done = await submain_menu_handler(user_menu_choice)
        else:
            break

# def recon_module(mode):
    # config = load_config()
    # if (mode == "automatic"):
        # bug_hunt_routine.start_bug_hunt_routine(
            # )
