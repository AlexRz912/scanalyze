import os

def file_exists(file, file_type="reg"):
    if (file_type == "folder"):
        return  os.path.isdir(file)
    return os.path.exists(file) 

