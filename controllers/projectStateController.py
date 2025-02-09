import time
from helpers import configHelper
from utils.fileUtils import existUtils 
# sont appelés à l'intérieur de l'action controller: 
# 2 actions déclenchent le set state
# load project

# start recon

def state_unset_new(project_config_path, project_config):
    project_config["new_project"] = False
    
    save_state(project_config_path, project_config)
    return project_config

def state_set_pending(project_config_path, project_config, is_diff):
    if is_diff:
        project_config["pending_recon"] = True

    save_state(project_config_path, project_config)
        
def state_unset_pending(project_config_path, project_config, success):
    if success:
        project_config["pending_recon"] = False
    
    save_state(project_config_path, project_config)
    return project_config

def project_new_state_set(project_config):
    print("from project new state set")
    print(project_config)
    
    return project_config["new_project"]

def is_pending_state_set(project_config):
    return project_config["pending_recon"]

def save_state(path, config):
    configHelper.save_config(path, config)

def httpx_results_exist(path):
    return existUtils.file_exists(path, "folder")

