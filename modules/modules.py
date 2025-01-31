import time
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

def handle_main_loop():
    user_input = main_menu_module()
    print(user_input)
    time.sleep(5)
    submain_menu_handler(user_input)

# def recon_module(mode):
    # config = load_config()
    # if (mode == "automatic"):
        # bug_hunt_routine.start_bug_hunt_routine(
            # )
