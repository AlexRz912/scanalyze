import os
from tool_wrapper import wrapper

bash_command = "awk '{print $1}' live_domains | anew livedomains_formatted"
wrapper(bash_command, "awk")

#most of it is very basic python