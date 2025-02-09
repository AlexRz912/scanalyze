import time
from .projectStateController import is_pending_state_set
from handlers.toolsHandlers.runToolsHandler import run_tools_handler

from config.configLoader import *
from utils.fileUtils import lineNumUtil

def recon_controller(project_path, project_config):

    domain_file_empty = is_domain_file_empty(f"{project_path}/domains")
    pending_recon = is_pending_state_set(project_config)
    success = run_tools_handler(domain_file_empty, pending_recon)

    return success

def is_domain_file_empty(path):
    return lineNumUtil.get_line_num(path) < 1