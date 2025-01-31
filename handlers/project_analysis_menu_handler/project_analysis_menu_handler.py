from modules.tool_modules import bug_hunt_routine
from config.config_loader import *

def handler():
    config = load_config()
    print("starting recon")
    bug_hunt_routine.start_bug_hunt_routine(
        config["project_path"], 
        config["tooling"], 
        config["output_path"], 
        config["input_path"]
    )