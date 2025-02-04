import os
import time
from helpers.configHelper import config_get

def start():
    print("asset_recon_module")
    tools = config_get("app", ["asset_recon_tools"])
    print("tools")
    path = config_get("app", ["project_path"])
    project_path = path["project_path"]
    for i in tools["asset_recon_tools"].keys():
        os.system(f"mkdir {project_path}/{i}")
        sh_exec(project_path, tools["asset_recon_tools"][i])

def sh_exec(path, tool):
    print(path)
    tool = tool.replace("project_path", path)
    os.system(tool)