def has_trailing_newline(file):
    with open(file, "rb") as f:  # Ouvre en mode binaire pour éviter les problèmes d'encodage
        f.seek(-1, 2)  # Déplace le curseur à l'avant-dernier octet du fichier
        last_char = f.read(1)  # Lit le dernier octet
    
    return last_char == b"\n"  # Vérifie si c'est un saut de ligne

def add_trailing_newline(file):
    with open(file, "a") as f:
        f.write("\n")