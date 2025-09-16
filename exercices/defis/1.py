# 1. On vous donne une liste de données de ventes, où chaque élément est un dictionnaire.
# 2. Créez un dictionnaire vide appelé `ventes_par_region`.
# 3. Parcourez `donnees_ventes`. Pour chaque vente, ajoutez le `montant` à la bonne région dans votre dictionnaire `ventes_par_region`.
# 4. Affichez le dictionnaire final `ventes_par_region` pour voir le total des ventes par région.
# Données : `donnees_ventes = [{'region': 'Nord', 'montant': 3500}, {'region': 'Sud', 'montant': 2000}, {'region': 'Nord', 'montant': 4200}, {'region': 'Ouest', 'montant': 2800}, {'region': 'Sud', 'montant': 3100}]`
# 💡 À l'intérieur de la boucle, vous devrez vérifier si une région est déjà une clé dans votre dictionnaire `ventes_par_region` en utilisant `region in ventes_par_region` ou `.get()`. Si non, ajoutez-la. Si oui, mettez à jour sa valeur.

donnees_ventes = [
    {'region': 'Nord', 'montant': 3500},
    {'region': 'Sud', 'montant': 2000},
    {'region': 'Nord', 'montant': 4200},
    {'region': 'Ouest', 'montant': 2800},
    {'region': 'Sud', 'montant': 3100}
]

ventes_par_region = {}

for vente in donnees_ventes:
    region = vente['region']
    montant = vente['montant']
    if region in ventes_par_region:
        ventes_par_region[region] += montant
    else:
        ventes_par_region[region] = montant

print(ventes_par_region)
