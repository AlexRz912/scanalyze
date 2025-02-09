from modules.assetReconModule import assetReconModule
from modules.domainReconModule import domainReconModule

from utils.ioUtils import inputUtils
def run_tools_handler(no_domains, pending):
    if no_domains:
        print("no domains provided, recon can't start, do you wish to add new domains? (y/n)")
        return
        # no domains provided, recon can't start, do you wish to add new domains
    if not pending:
        adding_new_domains_on_user_choice()
        # no new domains to scan for, do you wish to add new domains?
    else:
        assetReconModule.start()
        domainReconModule.start()
        # si la recon se passe mal, return False (on return True par défault)
        return True
    # return new_domains_provided
    
def adding_new_domains_on_user_choice():
    if user_wants_to_add_new_domains():
        assetReconModule.provide_new_domains()

def user_wants_to_add_new_domains():
    return inputUtils.get_choice("No recon pending, do you wish to add new domains (y/n or else)")

