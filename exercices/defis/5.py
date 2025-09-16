# 1. Vous avez deux listes : `departements` et `trimestres`.
# 2. Utilisez une boucle imbriquée (une boucle `for` à l'intérieur d'une autre) pour générer un résumé de rapport.
# 3. La boucle externe doit itérer sur les `departements`, et la boucle interne sur les `trimestres`.
# 4. Pour chaque combinaison, affichez une ligne comme : `Génération du rapport pour Ventes - T1`
# Données : `departements = ['Ventes', 'Marketing', 'IT']`, `trimestres = ['T1', 'T2', 'T3', 'T4']`
# 💡 La structure de votre code ressemblera à : `for departement in departements: ... for trimestre in trimestres: ...`

departements = ['Ventes', 'Marketing', 'IT']
trimestres = ['T1', 'T2', 'T3', 'T4']

for departement in departements:
    for trimestre in trimestres:
        print(f"Génération du rapport pour {departement} - {trimestre}")

    print("-" * 15)

