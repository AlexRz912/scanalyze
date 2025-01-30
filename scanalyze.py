from banner import display_banner
from modules import modules_handler

display_banner()


while (True):

    modules_handler.handle_menus("start_menu")
    modules_handler.recon_module("routine")
    # start_bug_hunt_routine(project_path, tooling, output_path, input_path)

