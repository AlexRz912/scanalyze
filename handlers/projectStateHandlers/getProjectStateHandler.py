import time

def get_project_state_handler(recon):
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