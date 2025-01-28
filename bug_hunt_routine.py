import os
import json
import subprocess
import set_mode
from config import config_handler

# is_manual_mode = set_mode.is_manual_mode()

config_path = config_handler.load_config_path()
config_file = config_handler.load_config_file(config_path)

working_path = config_handler.get_working_path(config_file)
project_path = config_handler.get_project_path(config_file)
tooling = config_handler.get_tooling(config_file)

output_path = config_handler.get_tool_output_path(config_file)
input_path = config_handler.get_tool_input_path(config_file)

def sh_exec(project_path, command, output_path, input_path):

    complete_input_path = (f"{project_path}/{input_path}")
    complete_output_path = (f"{project_path}/{output_path}")
    complete_folder = complete_output_path.replace("/results", "")
    command = command.replace("input_placeholder", complete_input_path)
    command = command.replace("output_placeholder", complete_output_path)
    
    os.system(f"mkdir {complete_folder}")
    os.system(command)
    # try:
        # result = subprocess.run(['which', tool], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # 
        # if result.returncode == 0:
            # os.system(command)
        # else:
            # print(f"Tool '{tool}' isn't installed")
    # except Exception as e:
        # print(f"Error while executing {tool} : {e}")

def start_bug_hunt_routine(project_path, tooling, output_path, input_path):
    # inclure un project path ici
    
    # if (is_manual_mode == True):
        # set_mode.manual_mode_instructions(command, tool)
    for tool in tooling.keys():
        sh_exec(project_path, tooling[tool], output_path[tool], input_path[tool])
        
