import time
from modules.assetReconModule import asset_recon_module
from modules.domainReconModule import domain_recon_module

def run_tools_handler(state):
    print(state)
    if not state["initial_asset_recon_completed"]: # supprimer la notion d'initial et indiquer que la recon est à refaire si il y a du pending recon
        print("starting_asset_recon ...")
        # va devoir chercher le premier outil d'asset recon depuis la config
        time.sleep(2)
    if not state["initial_domain_recon_completed"]: # supprimer la notion d'initial et indiquer à refaire si pending_recon
        print("starting_domain_recon ... ")
        # appelle domainReconModule en allant chercher le premier outil d'asset recon depuis
