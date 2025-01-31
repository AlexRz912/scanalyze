from views import main_menu
from handlers import menu_handler

def main_menu_module():
    main_menu.display_main_menu()
    return menu_handler.menu_main_handler("main")