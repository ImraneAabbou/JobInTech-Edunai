# 1. Recherchez dans la `file_commandes` la `commande_cible` ('CMD-103').
# 2. Si la commande est trouvée, affichez un message comme `Commande CMD-103 trouvée !` et arrêtez la recherche immédiatement.
# 3. Utilisez l'instruction `break` pour sortir de la boucle une fois la commande trouvée.
file_commandes = ['CMD-101', 'CMD-102', 'CMD-103', 'CMD-104', 'CMD-105']
commande_cible = 'CMD-103'

for commande in file_commandes:
    if commande == commande_cible:
        print(f"Commande {commande} trouvée !")
        break

