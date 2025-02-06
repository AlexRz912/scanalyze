import time
from modules.assetReconModule import assetReconModule
from modules.domainReconModule import domainReconModule

def run_tools_handler(state):
    new_domains_provided = False
    if not state["asset_recon_completed"] or state["pending_asset_recon"]: 
        assetReconModule.start()
    if not state["domain_recon_completed"] or state ["pending_domain_recon"]:
        domainReconModule.start()
    if state["add_new_domains"]:
        print("---------------------------------------------------")
        print("message from run tools handler in Run Tools Handler")
        print("if state add new domains is set, then we're asking for providing new domains")
        print("---------------------------------------------------")
        time.sleep(10)
        new_domains_provided = assetReconModule.provide_new_domains()
    return new_domains_provided