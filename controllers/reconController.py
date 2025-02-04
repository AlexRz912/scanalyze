from config.configLoader import *
from handlers.projectStateHandlers import projectStateHandler

from handlers.toolsHandlers.runToolsHandler import run_tools_handler

def recon_controller(config, project_config):
    state, add_new_domains = projectStateHandler.get_state(project_config["recon"])
    run_tools_handler(state, add_new_domains)