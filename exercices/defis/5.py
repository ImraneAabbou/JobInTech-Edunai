# Définissez un dictionnaire global `inventaire = {'ordinateur': 10, 'souris': 50, 'clavier': 20}`.
# Créez deux fonctions :
# 1. `ajouter_stock(produit, quantite)` : ajoute la `quantite` spécifiée au `produit` dans `inventaire`. Si le produit n'existe pas, l'ajoute.
# 2. `vendre_stock(produit, quantite)` : réduit la `quantite` du `produit`. S'assure que le stock ne devient pas négatif. Si la vente est réussie, retourne `True`, sinon `False` (avec un message d'erreur si stock insuffisant).
# Affichez l'inventaire après chaque opération pour démontrer le changement.
#
# Testez l'ajout de 5 'ordinateurs', la vente de 12 'souris', puis tentez de vendre 30 'clavier' (alors qu'il n'y en a que 20).
#
# 💡 Utilisez le mot-clé `global` dans les fonctions pour modifier le dictionnaire `inventaire`. Utilisez `.get()` avec une valeur par défaut pour les produits non existants.

inventaire = {'ordinateur': 10, 'souris': 50, 'clavier': 20}

def ajouter_stock(produit, quantite):
    global inventaire
    inventaire[produit] = inventaire.get(produit, 0) + quantite
    print(f"Ajouté {quantite} {produit}(s). Inventaire actuel: {inventaire}")

def vendre_stock(produit, quantite):
    global inventaire
    if inventaire.get(produit, 0) >= quantite:
        inventaire[produit] -= quantite
        print(f"Vendu {quantite} {produit}(s). Inventaire actuel: {inventaire}")
        return True
    else:
        print(f"Stock insuffisant pour {produit}. Inventaire actuel: {inventaire}")
        return False

# Tests
ajouter_stock('ordinateur', 5)
vendre_stock('souris', 12)
vendre_stock('clavier', 30)

