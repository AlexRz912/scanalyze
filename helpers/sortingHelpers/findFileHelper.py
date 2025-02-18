import os
import time

def find_and_print_to_temp(path, file, output_file):
    os.system(f"find {path} -type f -name \"{file}\" | anew {output_file}")

def find_folder_to_print(path, folder, output_file):
    os.system(f"find {path} -type d -name \"{folder}\" | anew {output_file}")

def find_file(path, file):
    return os.system(f"find {path} -type f -name \"{folder}\"")