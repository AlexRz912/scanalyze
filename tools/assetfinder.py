import os
from tool_wrapper import wrapper

command= "cat domains | assetfinder --subs-only | tee newmdomains"
wrapper(command, "assetfinder")

# bug > doesn't %0d%0a last line