# 1. Définir la fonction appliquer_reduction(prix, pourcentage_reduction).
# 2. À l'intérieur, appliquer la formule : prix * (1 - pourcentage_reduction / 100).
# 3. Retourner le résultat avec return.
# 4. Appeler la fonction avec prix = 150 et pourcentage_reduction = 15.
# 5. Afficher le prix après réduction.

def appliquer_reduction(prix, pourcentage_reduction):
    return prix * (1 - pourcentage_reduction / 100)

prix_reduit = appliquer_reduction(150, 15)
print(f"Le prix après réduction est : {prix_reduit} €")

