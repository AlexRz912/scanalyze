from views import start_menu
from helpers import menu_helper

def start_menu_module(config):
    start_menu.display_start_menu()
    return menu_helper.handle_start_menu_choice( 
        config["config_path"],
        config["config_file"], 
        config["working_path"], 
        config["project_path"]
    )

# handle_start_menu_choice got nothing to do in helpers
# a helper function should "help" the main function
# note that helpers are different from utilities because they're used in specific context