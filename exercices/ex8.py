# Commencez avec un nom de famille, par exemple, 'Dupont'
# Prenez la première lettre
# Ajoutez des astérisques '*' pour le reste du nom et affichez le résultat (ex: 'D*****')

# 💡 Combinez l'indexation [0], len(), et la multiplication de chaînes

nom = 'Dupont'
premier_lettre = nom[0]

secret_name = premier_lettre + ("#" * (len(nom) - 1) )

print(secret_name)
