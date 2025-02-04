import os
from helpers.domainFileHelpers import compareToPreviousHelper
from helpers.domainFileHelpers import buildDomainPathHelper
from helpers import configHelper
from utils.fileUtils import lineNumUtil
from utils.ioUtils import inputUtil

def get_state(recon):
    recon_state = {}
    add_new_domains = False
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

    if recon_state["initial_domain_recon_completed"] and recon_state["initial_asset_recon_completed"]:
        add_new_domains = inputUtil.get_input("do you wish to add new domains to search for new assets?")
    return recon_state, add_new_domains

def check_pending_domain_recon(pending):
    if (pending == 1):
        return inputUtil.get_input("new domains were brought for recon, do you wish to discover content? (y/else)\n")

def check_pending_asset_recon(pending):
    if (pending == 1):
        return inputUtil.get_input("new assets were brought for recon, do you wish to discover new assets (y/else)\n")

def start_asset_recon_or_continue(do_recon, state): # -> reconHelpers in near future
    if do_recon:
        return True
    return False

def start_domain_recon_or_continue(do_recon, state): # -> reconHelpers in near future
    if do_recon:
        return True
    return False

def set_state(project_config_path, path, project_recon):
    if domains_file_empty(path):
        raise ValueError("Domains file is empty, please provide domains to your project domain file, one domain per line")

    set_domain_recon_state(project_config_path, path, project_recon)       
    set_asset_recon_state(project_config_path, path, project_recon)

    is_different = domain_file_is_different(path)
    set_pending_state(project_config_path, project_recon, is_different)

def set_domain_recon_state(config_path, path, recon):
    if os.path.isdir(f"{path}/gf"):
        recon["recon"]["domain_recon"]["initial_recon_completed"] = 1
    else:
        recon["recon"]["domain_recon"]["initial_recon_completed"] = 0
    configHelper.save_config(config_path, recon)

def set_asset_recon_state(config_path, path, recon):
    if os.path.isdir(f"{path}/assetfinder"):
        recon["recon"]["asset_recon"]["initial_recon_completed"] = 1
    else:
        recon["recon"]["asset_recon"]["initial_recon_completed"] = 0
    configHelper.save_config(config_path, recon)

def set_pending_state(config_path, recon, is_diff):
    if is_diff:
        recon["recon"]["asset_recon"]["pending_recon"] = 1
    else:
        recon["recon"]["asset_recon"]["pending_recon"] = 0
    configHelper.save_config(config_path, recon)

def domain_file_is_different(path):
    previous_domain_file = buildDomainPathHelper.build_path(path, False)
    new_domain_file = buildDomainPathHelper.build_path(path, True)

    new_file_line_num = lineNumUtil.get_line_num(new_domain_file)
    previous_file_line_num = lineNumUtil.get_line_num(previous_domain_file)

    return compareToPreviousHelper.compare(new_file_line_num, previous_file_line_num)

def domains_file_empty(path):
    domain_file = buildDomainPathHelper.build_path(path, True)
    return True if lineNumUtil.get_line_num(domain_file) < 2 else False