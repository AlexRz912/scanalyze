from views import menu_view
from helpers import menu_helper
from config.config_loader import *

def main_menu():
    menu_view.display_start_menu()
    menu_helper.handle_start_menu_choice(config_path, config_file, working_path, project_path)

