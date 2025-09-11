# Utilisez la chaîne de SKU suivante : 'LAP-2024-PRO'
# Extrayez le type de produit ('LAP'), l'année ('2024') et le modèle ('PRO') dans des variables distinctes
# Affichez chaque composant sur une ligne séparée

# 💡 Le découpage de chaîne [start:end] est la clé ici. Rappelez-vous que l'indexation commence à 0

product = 'LAP-2024-PRO'.split("-")

print(f"""\
nom: {product[0]}
annee: {product[1]}
model: {product[2]}
""")
