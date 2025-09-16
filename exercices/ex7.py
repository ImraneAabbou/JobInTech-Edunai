# 1. Initialisez une variable `compteur` à 10.
# 2. Utilisez une boucle `while` qui continue tant que `compteur` est supérieur à 0.
# 3. À l'intérieur de la boucle, affichez la valeur actuelle du compteur, puis diminuez-la de 1.
# 4. Après la boucle, affichez 'Décollage !'.
# Aucune liste de données initiale nécessaire. Définissez simplement `compteur = 10`.
# 💡 Souvenez-vous des trois parties d'une boucle while : initialisation (`compteur = 10`), condition (`while compteur > 0`), et mise à jour (`compteur = compteur - 1`).

compteur = 10

while compteur > 0:
    print(compteur)
    compteur -= 1

print("Décollage !")

