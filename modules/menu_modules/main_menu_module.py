from views import menu_view
from helpers import menu_helper


def main_menu(config):
    menu_view.display_start_menu()
    menu_helper.handle_start_menu_choice(
        config["config_path"], 
        config["config_file"], 
        config["working_path"], 
        config["project_path"]
    )

