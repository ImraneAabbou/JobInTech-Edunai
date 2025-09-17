# 1. Définir la fonction obtenir_nom_complet(prenom, nom).
# 2. Retourner une chaîne formatée 'Prénom Nom' avec .title().
# 3. Tester avec prenom='jean' et nom='dupont'.

def obtenir_nom_complet(prenom, nom):
    return f"{prenom.title()} {nom.title()}"

# Test
nom_complet = obtenir_nom_complet("jean", "dupont")
print(nom_complet)

