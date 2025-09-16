# 1. Vous avez une liste de `transactions` qui inclut des entrées invalides (négatives).
# 2. Utilisez une boucle `for` et l'instruction `continue` pour calculer la somme des transactions valides uniquement.
# 3. Comptez également combien de transactions invalides ont été sautées.
# 4. Affichez le total des transactions valides et le nombre d'invalides.
transactions = [200, 50, -10, 300, -5, 75]

total_valides = 0
invalides = 0

for montant in transactions:
    if montant < 0:
        invalides += 1
        continue
    total_valides += montant

print(f"Total des transactions valides : {total_valides}")
print(f"Nombre de transactions invalides : {invalides}")

