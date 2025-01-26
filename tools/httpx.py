import os
from tool_wrapper import wrapper

bash_command = "cat newmdomains | httpx -follow-host-redirects -title -status-code -cdn -tech-detect | tee live_domains"
wrapper(bash_command, "httpx")
    
    

