from helpers import config_helper

def load_config():
    config = {}
    config = config_helper.load_config_path()
    return config
