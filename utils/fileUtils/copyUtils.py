import os
import time

def copy_directory_into_folder(directory, project_path, folder):
    print(f"cp -r {directory} {project_path}/{folder}/")
    time.sleep(3)
    os.system(f"cp -r {directory} {project_path}/{folder}/")

def copy_file_into_folder(file, project_path, folder):
    file = file.replace("\n", "")
    print(f"cp {file} {project_path}/{folder}/")
    time.sleep(3)
    os.system(f"cp {file} {project_path}/{folder}/")