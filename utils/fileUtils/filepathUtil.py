import os

def get_current_dir(file_path):
    return os.path.dirname(file_path)

def get_subdirectory(path):
    return os.path.basename(path)