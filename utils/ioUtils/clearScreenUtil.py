import os

def clear_screen_util():
    os.system("cls" if os.name == "nt" else "clear")