import os
import subprocess


is_manual_mode = set_mode.is_manual_mode()


def wrapper(command, tool, project_path):
    if (is_manual_mode == True):
        set_mode.manual_mode_instructions(command, tool)
    try:
        result = subprocess.run(['which', tool], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            print(f"Starting {tool}")
            os.system(command)
        else:
            print(f"Tool {tool} isn't installed")
    except Exception as e:
        print(f"Erreur lors de l'exécution : {e}")



