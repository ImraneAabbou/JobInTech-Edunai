# 1. Créez une liste vide appelée `noms_utilisateurs`.
# 2. Parcourez la liste `noms_employes`.
# 3. Pour chaque nom, créez un nom d'utilisateur en prenant le nom en minuscules et en ajoutant '@entreprise.com'.
# 4. Ajoutez le nouveau nom d'utilisateur à la liste `noms_utilisateurs`.
# 5. Affichez la liste finale `noms_utilisateurs`.
# Données : `noms_employes = ['Alice', 'Bob', 'Charlie']`
# 💡 Utilisez la méthode de chaîne `.lower()` sur chaque nom à l'intérieur de la boucle.

noms_employes = ['Alice', 'Bob', 'Charlie']
noms_utilisateurs = []

for nom in noms_employes:
    noms_utilisateurs.append(nom.lower() + '@entreprise.com')

print(noms_utilisateurs)

