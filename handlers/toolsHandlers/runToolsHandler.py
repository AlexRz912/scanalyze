import time
from modules.assetReconModule import assetReconModule
from modules.domainReconModule import domainReconModule

def run_tools_handler(state):
    print(state)
    if not state["asset_recon_completed"] or state["pending_asset_recon"]: 
        assetReconModule.start()
    if not state["domain_recon_completed"] or state ["pending_domain_recon"]:
        domainReconModule.start()
    if state["add_new_domains"]:
        assetReconModule.provide_new_domains()