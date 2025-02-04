from config.configLoader import *
from handlers.projectStateHandlers.getProjectStateHandler import *
from handlers.projectStateHandlers.setProjectStateHandler import *

from handlers.toolsHandlers.runToolsHandler import run_tools_handler

def recon_controller():

    config = load_config("app")
    project_config = load_config("project")

    set_project_state_handler(config["project_path"], project_config)

    state = get_project_state_handler(project_config["recon"])
    run_tools_handler(state)