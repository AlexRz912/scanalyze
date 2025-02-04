import asyncio
from .actionController import action_controller

# from handlers.submain_menu_handler import submain_menu_handler

from config.configLoader import *



def run_main_loop(start):
    while (True):
        start_action = None
        if start:
            start_action = action_controller("start")
        start = False
        if (start_action == "3"):
            continue
        elif (start_action == "quit"):
            break
        main_action = action_controller("main")
        if (main_action == "5"):
            break