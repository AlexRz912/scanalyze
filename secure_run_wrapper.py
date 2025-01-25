import os
import subprocess


def wrapper(command, tool):
    try:
        result = subprocess.run(['which', tool], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            print(f"Starting tool '{tool}'")
            os.system(command)
            os.system("echo 'let it cook'")
        else:
            print(f"Tool '{tool}' isn't installed")
    except Exception as e:
        print(f"Erreur lors de l'exécution : {e}")



