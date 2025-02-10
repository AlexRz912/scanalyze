import os

def message_concat_util(messages):
    return ", and ".join(messages)

def tree_folders(path):
    os.system(f"tree {path}")