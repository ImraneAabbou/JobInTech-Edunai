#     Créez une classe `Client`.
#     Utilisez la méthode `__init__` pour initialiser `id_client`, `nom` et `email` lorsqu'un objet est créé.
#
# Créez un client avec l'ID 101, le nom 'Alice' et l'email 'alice@example.com'.
#
# 💡 La méthode `__init__` est la manière standard de définir les attributs initiaux d'un objet.

class Client:
    def __init__(self, _id, nom, email):
        self.id = _id
        self.nom = nom
        self.email = email

c = Client(1, "Someone", "someone@somewhere.com")
