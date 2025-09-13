#    Créez une liste avec 5 noms de produits (ordinateurs portables, souris, claviers, moniteurs, imprimantes)
#    Ajoutez 2 nouveaux produits à la fin de la liste
#    Affichez le nombre total de produits ainsi que le premier et le dernier produit
#
#💡 Utilisez append() pour ajouter des éléments et len() pour compter


produits = ['ordinateurs portables', "souris", "claviers", "moniteurs", "imprimantes"]

produits.append("Something 1")
produits.append("Something 2")

total_produits = len(produits)

print("total:", total_produits)
