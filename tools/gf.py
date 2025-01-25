import os
from secure_run_wrapper import wrapper

os.system("cd roots")
bash_command = "gf meg-headers | sort -u > headers"
wrapper(bash_command, "gf")