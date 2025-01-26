import os
from banner import display_banner
import menu

display_banner()

# the following steps are hardcoded here and are not dynamically handled

user_keeps_working = True

while (user_keeps_working):

    menu.display_project_menu()
    menu.display_mode_menu()
    # it does reload the whole loop, without taking core of the imports
    from tools import assetfinder
    from tools import httpx
    import save
    from tools import awk
    from tools import fff
    from tools import gf

    keep_working_flag = input("Continue working? (y/else)")
    if (keep_working_flag.lower() != "y"):
        user_keeps_working = False
