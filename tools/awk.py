import os
from secure_run_wrapper import wrapper

bash_command = "awk '{print $1}' live_domains | anew livedomains_formatted"
wrapper(bash_command, "awk")