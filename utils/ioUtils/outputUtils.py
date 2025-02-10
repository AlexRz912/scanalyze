import os

def message_concat_util(messages):
    return ", and ".join(messages)

def tree_folders(path):
    os.system(f"tree {path}")

def print_file_content(file_path):
    os.system(f"cat {file_path}")

def find_file(path, file):
    os.system(f"find {path} -type f -name '{file}")