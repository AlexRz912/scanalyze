from handlers import config_handler

config_path = config_handler.load_config_path()
config_file = config_handler.load_config_file(config_path)

working_path = config_handler.get_working_path(config_file)
project_path = config_handler.get_project_path(config_file)
tooling = config_handler.get_tooling(config_file)

output_path = config_handler.get_tool_output_path(config_file)
input_path = config_handler.get_tool_input_path(config_file)