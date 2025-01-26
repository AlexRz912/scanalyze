class CustomDict:
    def __init__(self):
        self._keys = []
        self._values = {}

    def __repr__(self):
        return str({key: self._values[key] for key in self._keys})

    def insert(self, key, value, position=None):
        """Insère une clé à une position spécifique (ou à la fin par défaut)."""
        if key in self._values:
            raise KeyError(f"La clé '{key}' existe déjà.")
        
        if position is None or position >= len(self._keys):
            self._keys.append(key)
        else:
            self._keys.insert(position, key)
        
        self._values[key] = value

    def delete(self, key):
        """Supprime une clé."""
        if key in self._values:
            self._keys.remove(key)
            del self._values[key]
        else:
            raise KeyError(f"La clé '{key}' n'existe pas.")

    def get(self, key):
        """Récupère une valeur via une clé."""
        return self._values.get(key, None)

    def items(self):
        """Retourne les clés et valeurs dans l'ordre."""
        return [(key, self._values[key]) for key in self._keys]

    def update(self, key, value):
        """Modifie la valeur d'une clé existante."""
        if key in self._values:
            self._values[key] = value
        else:
            raise KeyError(f"La clé '{key}' n'existe pas.")


# Creates custom data structure
data = CustomDict()

# Adds Keys
data.insert("clé1", "valeur1")
data.insert("clé2", "valeur2")
data.insert("clé3", "valeur3")

# Insert keys between 
data.insert("clé1.5", "valeur1.5", position=1)

# Outputs dict
print("Dictionnaire après insertion :", data)

# Updates a value
data.update("clé1.5", "nouvelle_valeur1.5")

# Deletes a key
data.delete("clé2")

# Retrieve elements in order
print("Clés et valeurs :", data.items())

# Retrieves a specific value
print("Valeur de 'clé1.5' :", data.get("clé1.5"))
