import os
import time
def find_and_print_to_temp(path, file):
    os.system(f"find {path} -type f -name \"{file}\" | anew {path}/temp")

def find_folder_to_print(path, folder):
    os.system(f"find {path} -type d -name \"{folder}\" | anew {path}/temp")