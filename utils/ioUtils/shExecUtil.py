import os

def exec(path, tool):
    tool = tool.replace("project_path", path)
    os.system(tool)

def cmd_exec(cmd):
    os.system(cmd)