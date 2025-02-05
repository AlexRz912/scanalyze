from utils.ioUtils import inputUtils

def do_pending(do_recon):
    return do_recon

def ask_for_domain_recon(recon):
    if recon:
        return inputUtils.get_choice("New live assets were brought for recon, do you wish to poke at them (y/n)")
    return False
def ask_for_asset_recon(recon):
    if recon:
        return inputUtils.get_choice("New domains were brought for recon, do you wish to search for assets (y/n)")
    return False