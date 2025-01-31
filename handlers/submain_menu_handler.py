import asyncio
from handlers.project_analysis_menu_handler import project_analysis_menu_handler

async def submain_menu_handler(choice):
    if (choice == "1"):
        project_analysis_menu_handler.handler()
        return True
    elif (choice == ""):
        return
    elif (choice == ""):
        return
    elif (choice == ""):
        return
    elif (choice == "quit"):
        return
