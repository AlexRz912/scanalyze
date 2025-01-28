import os
from tool_wrapper import wrapper
from config import config_handler

config_path = config_handler.load_config_path()
config_file = config_handler.load_config_file(config_path)

working_path = config_handler.get_working_path(config_file)
project_path = config_handler.get_project_path(config_file)

command= (f"cat {project_path}/domains | assetfinder --subs-only | tee {project_path}/newmdomains")
wrapper(command, "assetfinder")

# bug > doesn't %0d%0a last line