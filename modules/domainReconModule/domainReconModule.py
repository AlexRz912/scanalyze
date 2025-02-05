import os
from helpers.configHelper import config_get
from utils.ioUtils import shExecUtil


def start():
    tools = config_get("app", ["domain_recon_tools"])
    path = config_get("app", ["project_path"])
    project_path = path["project_path"]
    for i in tools["domain_recon_tools"].keys():
        os.system(f"mkdir {project_path}/{i}")
        shExecUtil.exec(project_path, tools["domain_recon_tools"][i])