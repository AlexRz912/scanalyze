import time
from modules.assetReconModule import assetReconModule
from modules.domainReconModule import domainReconModule

def run_tools_handler(state, add_new_domains):
    print(state)
    if not state["initial_asset_recon_completed"]: # supprimer la notion d'initial et indiquer que la recon est à refaire si il y a du pending recon
        assetReconModule.start()
    if not state["initial_domain_recon_completed"]: # supprimer la notion d'initial et indiquer à refaire si pending_recon
        domainReconModule.start()
        # appelle domainReconModule en allant chercher le premier outil d'asset recon depuis
    if add_new_domains:
        print("bah on va appeler la fonction qui permet d'ajouter des domaines !")