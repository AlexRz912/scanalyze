import os
from banner import display_banner
from modules import modules_handler
from bug_hunt_routine import start_bug_hunt_routine

display_banner()

from views.config_view import *


while (True):

    
    modules_handler.display_start_menu()
    modules_handler.handle_start_menu_choice(config_path, config_file, working_path, project_path)
    
    # start_bug_hunt_routine(project_path, tooling, output_path, input_path)

    # YAGNI principle :D
    # menu.display_mode_menu()

    # from tools import assetfinder
    # from tools import httpx
    # import save
    # from tools import awk
    # from tools import fff
    # from tools import gf

