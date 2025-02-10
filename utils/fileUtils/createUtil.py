import os

def create_file(filepath):
    os.system(f"touch {filepath}")

def create_folder(folder):
    os.system(f"mkdir {folder}")