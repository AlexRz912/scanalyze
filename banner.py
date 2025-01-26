import pyfiglet

def display_banner():
    # Générer une bannière stylisée
    banner = pyfiglet.figlet_format("Scanalyze")
    version = "v0"
    print("\033[92m" + banner + "\033[0m")  # Couleur verte
    print("\033[94m" + f"{' ' * 20}{version}" + "\033[0m")  # Couleur bleue
    

    
