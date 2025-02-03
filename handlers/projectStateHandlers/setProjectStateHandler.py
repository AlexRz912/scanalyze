import os

def set_project_state_handler(path, project_recon):
    if os.path.isdir(f"{path}/fff/results"):
        set_domain_recon_state(project_recon)
    if os.path.isdir(f"{path}/assetfinder"):
        set_asset_recon_state(project_recon)
    
def set_domain_recon_state(recon):
    recon["recon"]["domain_recon"]["initial_recon_completed"] = 1

def set_asset_recon_state(recon):
    recon["recon"]["asset_recon"]["initial_recon_completed"] = 1

