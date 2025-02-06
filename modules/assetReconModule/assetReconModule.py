import os
import time

from helpers.configHelper import config_get
from helpers.domainFileHelpers import appendToHelper
from helpers.domainFileHelpers import extractFromListHelper
from helpers.domainFileHelpers import duplicateDomainHelper

from utils.fileUtils import existUtils
from utils.fileUtils import getPathUtil
from utils.fileUtils import trailingNewlineUtils 

from utils.ioUtils import inputUtils
from utils.ioUtils import shExecUtil

from utils.parsingUtils import whitespaceUtils

def start():
    tools = config_get("app", ["asset_recon_tools"])
    path = config_get("app", ["project_path"])
    project_path = path["project_path"]
    for i in tools["asset_recon_tools"].keys():
        os.system(f"mkdir {project_path}/{i}")
        shExecUtil.exec(project_path, tools["asset_recon_tools"][i])

def provide_new_domains(newly_created=False):
    
    if newly_created:
        print("-------------------------------------------------")
        print("message from provide_new_domains in assetReconModule")
        print("when project is newly created, it asks to add domains to the domain file")
        print("-------------------------------------------------")
        time.sleep(5)
        print("You need to add domains to the domain file, you can do it here or manually later.")
        
    else:
        print("-------------------------------------------------")
        print("message from provide_new_domains in assetReconModule")
        print("when user wants to provide new domains, it is called from ")
        print("-------------------------------------------------")
        time.sleep(5)

    path = config_get("app", ["project_path"])
    domain_path = getPathUtil.build_path(path["project_path"], "domains")
    if existUtils.file_exists(domain_path):
        provided_domains = inputUtils.get_input("Provide a comma separated list of domains")
        provided_domains = whitespaceUtils.remove_whitespaces(provided_domains)

        while not provided_domains == "":
            provided_domains, domain = extractFromListHelper.get_first_domain(provided_domains)
            if not newly_created:
                if not trailingNewlineUtils.has_trailing_newline(domain_path):
                    trailingNewlineUtils.add_trailing_newline(domain_path)
                if not duplicateDomainHelper.is_dupe(domain_path, domain):
                    appendToHelper.append_to(domain_path, domain)
            appendToHelper.append_to(domain_path, domain)
        return True
    else:
        raise ValueError("The domain file doesn't exist")
    return False