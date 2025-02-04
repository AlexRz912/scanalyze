import os
from helpers.domainFileHelpers import compareToPreviousHelper
from helpers import configHelper
from utils.fileUtils import lineNumUtil

def get_state(recon):
    recon_state = {}

    recon_state["initial_domain_recon_completed"] = False
    recon_state["initial_asset_recon_completed"] = False
    
    if (recon["domain_recon"]["initial_recon_completed"] == 1):
        print("you've already gathered data for specific domains")
        recon_state["initial_domain_recon_completed"] = True

    if (recon["asset_recon"]["initial_recon_completed"] == 1):
        print("you've already gathered data in relation to provided scope")
        recon_state["initial_asset_recon_completed"] = True

    pending_recon_exists = check_pending_domain_recon(recon["domain_recon"]["pending_recon"])
    pending_recon_exists = check_pending_asset_recon(recon["asset_recon"]["pending_recon"])

    recon_state["pending_domain_recon"] = start_domain_recon_or_continue(pending_recon_exists, recon_state)
    recon_state["pending_asset_recon"] = start_asset_recon_or_continue(pending_recon_exists, recon_state)
    
    return recon_state

def check_pending_domain_recon(pending):
    if (pending == 1):
        print("new domains were brought for recon, do you wish to discover content? (y/else)\n")
        choice = input()
        return True if choice == "y" else False
def check_pending_asset_recon(pending):
    if (pending == 1):
        print("new assets were brought for recon, do you wish to discover new assets (y/else)\n")
        choice = input()
        return True if choice == "y" else False

def start_asset_recon_or_continue(do_recon, state):
    if do_recon:
        return True
    return False

def start_domain_recon_or_continue(do_recon, state):
    if do_recon:
        return True
    return False

def set_state(project_config_path, path, project_recon):
    if os.path.isdir(f"{path}/gf"):
        set_domain_recon_state(project_config_path, project_recon)       
    if os.path.isdir(f"{path}/assetfinder"):
        set_asset_recon_state(project_config_path, project_recon)
    if compare_to_previous_domain_file(path):
        set_pending_state("asset", project_recon)

    
def set_domain_recon_state(path, recon):
    recon["recon"]["domain_recon"]["initial_recon_completed"] = 1
    configHelper.save_config(path, recon)

def set_asset_recon_state(path, recon):
    recon["recon"]["asset_recon"]["initial_recon_completed"] = 1
    configHelper.save_config(path, recon)

def set_pending_state(recon_type, recon):
    return

def compare_to_previous_domain_file(path):
    previous_domain_file = path + "/previous/domains"
    new_domain_file = path + "/domains"

    new_file_line_num = lineNumUtil.get_line_num(new_domain_file)
    previous_file_line_num = lineNumUtil.get_line_num(previous_domain_file)

    return compareToPreviousHelper.compare(new_file_line_num, previous_file_line_num)