import os
from tool_wrapper import wrapper

os.system("cd roots")
bash_command = "find ./roots -type f -name \"*.headers\" -exec cat {} + | gf meg-headers | sort -u > headers"
wrapper(bash_command, "gf")