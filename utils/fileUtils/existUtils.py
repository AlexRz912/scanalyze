import os

def file_exists(file, file_type="reg"):
    if (file_type == "folder"):
        return True if os.path.isdir(file) else False
    return True if os.path.exists(file) else False

