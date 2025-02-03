
import asyncio
from .actionController import action_controller

# from handlers.submain_menu_handler import submain_menu_handler

from config.configLoader import *

action = action_controller("start")

def run_main_loop():
    while (True):
        if (action == "3"):
            continue
        elif (action == "quit"):
            break
        user_menu_choice = action_controller("main")