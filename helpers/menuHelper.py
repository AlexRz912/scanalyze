from . import projectsHelper

def list_projects_into_action(path, action):
    projectsHelper.list_projects(path)
    return projectsHelper.select_project(action)