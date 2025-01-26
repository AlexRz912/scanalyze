import os
from tool_wrapper import wrapper

bash_command = "cat livedomains_formatted | fff -d 1 -S -o roots"
wrapper(bash_command, "fff")