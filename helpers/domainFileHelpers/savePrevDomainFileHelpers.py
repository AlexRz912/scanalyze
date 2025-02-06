import os
import time
def save(path, domain_file):
    os.system(f"mkdir {path}")
    os.system(f"cp {domain_file} {path}/domains")

def previous_folder_exists(path):
    return os.path.isdir(path)