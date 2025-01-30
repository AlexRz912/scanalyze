from helpers import config_helper

config_path = config_helper.load_config_path()
config_file = config_helper.load_config_file(config_path)

working_path = config_helper.get_working_path(config_file)
project_path = config_helper.get_project_path(config_file)
tooling = config_helper.get_tooling(config_file)

output_path = config_helper.get_tool_output_path(config_file)
input_path = config_helper.get_tool_input_path(config_file)
