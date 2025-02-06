import os
import time

from modules.assetReconModule import assetReconModule
from helpers.reconHelpers import pendingReconHelper
from helpers.reconHelpers import reconStateHelpers
from helpers.domainFileHelpers import compareToPreviousHelper
from helpers.domainFileHelpers import buildDomainPathHelper
from helpers import configHelper
from utils.fileUtils import lineNumUtil
from utils.ioUtils import inputUtils

def get_state(recon):

    print("--------------- verifying what state looks like ----------------")
    print(recon)
    print("--------------- verifying what state looks like ----------------")
    time.sleep(2)
    recon_state = {}
    
    recon_state["domain_recon_completed"] = reconStateHelpers.get_recon_state(recon["domain_recon"]["initial_recon_completed"])
    recon_state["asset_recon_completed"] = reconStateHelpers.get_recon_state(recon["asset_recon"]["initial_recon_completed"])
    recon_state["add_new_domains"] = False

    if recon_state["asset_recon_completed"]:
        reconStateHelpers.print_asset_recon_completed()
    if recon_state["domain_recon_completed"]:
        reconStateHelpers.print_domain_recon_completed()  
    
    domain_recon_state = reconStateHelpers.get_recon_state(recon["domain_recon"]["pending_recon"])
    do_domain_recon = pendingReconHelper.ask_for_domain_recon(domain_recon_state)

    asset_recon_state = reconStateHelpers.get_recon_state(recon["asset_recon"]["pending_recon"])
    do_asset_recon = pendingReconHelper.ask_for_asset_recon(asset_recon_state)
    
    recon_state["pending_domain_recon"] = pendingReconHelper.do_pending(do_domain_recon)
    recon_state["pending_asset_recon"] = pendingReconHelper.do_pending(do_asset_recon)

    do_pending = False

    if do_domain_recon or do_asset_recon:
        do_pending = True

    if recon_state["domain_recon_completed"] and recon_state["asset_recon_completed"] and not do_pending:
        recon_state["add_new_domains"] = inputUtils.get_choice("do you wish to add new domains to search for new assets?")

    return recon_state

def start_asset_recon_or_continue(do_recon, state): # -> reconHelpers in near future
    if do_recon:
        return True
    return False

def start_domain_recon_or_continue(do_recon, state): # -> reconHelpers in near future
    if do_recon:
        return True
    return False

def set_state(project_config_path, path, project_recon, is_diff):
    if domains_file_empty(path):
        assetReconModule.provide_new_domains(True)

    set_domain_recon_state(project_config_path, path, project_recon)  

    print("--------------------------------------------------------------")  
    print("state after set_domain_recon_state")  
    print(project_recon)
    time.sleep(2)
    print("--------------------------------------------------------------")  

    set_asset_recon_state(project_config_path, path, project_recon)

    print("--------------------------------------------------------------")  
    print("state after set_asset_recon_state")  
    print(project_recon)
    time.sleep(2)
    print("--------------------------------------------------------------")  
        
    set_new_state_to_false(project_config_path, project_recon)

    print("--------------------------------------------------------------")  
    print("state after set_new_state_to_false")  
    print(project_recon)
    time.sleep(2)
    print("--------------------------------------------------------------") 
    
    set_pending_state(project_config_path, project_recon, is_diff)
    print("--------------------------------------------------------------")  
    print("state after set_pending_state")  
    print(project_recon)
    time.sleep(2)
    print("--------------------------------------------------------------") 

def set_new_state_to_false(config_path, recon):
    recon["new_project"] = False 
    configHelper.save_config(config_path, recon)

def set_domain_recon_state(config_path, path, recon):
    if os.path.isdir(f"{path}/gf"): # besoin du path ici pour chercher le dossier
        recon["recon"]["domain_recon"]["initial_recon_completed"] = 1
    else:
        recon["recon"]["domain_recon"]["initial_recon_completed"] = 0
    configHelper.save_config(config_path, recon)

def set_asset_recon_state(config_path, path, recon):
    if os.path.isdir(f"{path}/assetfinder"): # besoin du path ici pour chercher le dossier
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
    return lineNumUtil.get_line_num(domain_file) < 1

def save_state(config_path, path, recon, is_new_project=False, is_diff=False):
    if is_diff:
        recon["recon"]["asset_recon"]["pending_recon"] = 1
    else:
        recon["recon"]["asset_recon"]["pending_recon"] = 0
    configHelper.save_config(config_path, recon)

def is_a_dir(path): # post v1: This is an util that will be used when converting recon state values to booleans 
    return os.path.isdir(path)

def is_new_project(config):
    return config["new_project"]

def create_previous_domain_file():
    return