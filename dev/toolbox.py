from collections import OrderedDict

# Exemple d'utilisation d'OrderedDict
data = OrderedDict([
    ("assetfinder", "cat domains | assetfinder --subs-only | tee newmdomains"),
    ("httpx", "cat newmdomains | httpx -follow-host-redirects -title -status-code -cdn -tech-detect | tee live_domains"),
    ("awk", "awk '{print $1}' live_domains | anew livedomains_formatted"),
    ("fff", "cat livedomains_formatted | fff -d 1 -S -o roots"),
    ("gf", "find ./roots -type f -name \"*.headers\" -exec cat {} + | gf meg-headers | sort -u > headers")
])

# Accéder aux clés et valeurs
for key, value in data.items():
    print(f"Clé: {key}, Valeur: {value}")

# Accéder directement à une clé
print(data["httpx"])  # Output: valeur2


    def edit(toolname)