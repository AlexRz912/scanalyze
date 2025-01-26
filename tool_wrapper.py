import os
import subprocess
from set_mode import is_manual_mode

def manual_mode_instructions(command, tool):
    user_answer = input(f"Do you want to run {tool} with the following flags? : {command}\nor a customize it (y/else)\n")
    if (user_answer.lower() == 'y'):
        custom_flags = input()
        return custom_flags

def wrapper(command, tool):
    if (is_manual_mode):
        manual_mode_instructions(command, tool)
    
    try:
        result = subprocess.run(['which', tool], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            print(f"Starting tool '{tool}'")
            os.system(command)
        else:
            print(f"Tool '{tool}' isn't installed")
    except Exception as e:
        print(f"Erreur lors de l'exécution : {e}")



