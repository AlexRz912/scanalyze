import os
from banner import display_banner
import menu
import projects_handler
from config import config_handler
from bug_hunt_routine import start_bug_hunt_routine

display_banner()

config_path = config_handler.load_config_path()
config_file = config_handler.load_config_file(config_path)

working_path = config_handler.get_working_path(config_file)
project_path = config_handler.get_project_path(config_file)
tooling = config_handler.get_tooling(config_file)

output_path = config_handler.get_tool_output_path(config_file)
input_path = config_handler.get_tool_input_path(config_file)

while (True):

    if (not config_handler.check_working_path_exists(working_path)):
        break
    menu.display_start_menu()
    menu.handle_start_menu_choice(config_path, config_file, working_path, project_path)
    

    start_bug_hunt_routine(project_path, tooling, output_path, input_path)

    # YAGNI principle :D
    # menu.display_mode_menu()

    # from tools import assetfinder
    # from tools import httpx
    # import save
    # from tools import awk
    # from tools import fff
    # from tools import gf

