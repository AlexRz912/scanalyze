import pyfiglet

def display_banner():
    banner = pyfiglet.figlet_format("Scanalyze")
    version = "v0"
    print("\033[92m" + banner + "\033[0m")
    print("\033[94m" + f"{' ' * 20}{version}" + "\033[0m")
    

    
