# 1. Vous avez une liste de données clients.
# 2. Créez deux listes vides : `clients_a_haute_valeur` et `clients_standards`.
# 3. Parcourez la liste `clients`. Si le `total_depense` d'un client est supérieur à 1000, ajoutez son `nom` à la liste `clients_a_haute_valeur`. Sinon, ajoutez son nom à la liste `clients_standards`.
# 4. Affichez les deux listes à la fin.
# Données : `clients = [{'nom': 'Alice', 'total_depense': 1250}, {'nom': 'Bob', 'total_depense': 850}, {'nom': 'Charlie', 'total_depense': 2100}, {'nom': 'David', 'total_depense': 500}]`
# 💡 Une boucle `for` avec une instruction `if/else` à l'intérieur est parfaite pour cela. Utilisez `.append()` pour ajouter des noms à vos nouvelles listes.

clients = [
    {'nom': 'Alice', 'total_depense': 1250},
    {'nom': 'Bob', 'total_depense': 850},
    {'nom': 'Charlie', 'total_depense': 2100},
    {'nom': 'David', 'total_depense': 500}
]

clients_a_haute_valeur = []
clients_standards = []

for client in clients:
    if client['total_depense'] > 1000:
        clients_a_haute_valeur.append(client['nom'])
    else:
        clients_standards.append(client['nom'])

print(clients_a_haute_valeur)
print(clients_standards)

