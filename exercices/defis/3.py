# Créez une fonction `nettoyer_donnees(liste_chaines, supprimer_vides=True, convertir_minuscules=False)`.
# La fonction prend une liste de chaînes de caractères.
# `supprimer_vides` (booléen, par défaut `True`) : si `True`, retire toutes les chaînes vides ou composées uniquement d'espaces.
# `convertir_minuscules` (booléen, par défaut `False`) : si `True`, convertit toutes les chaînes restantes en minuscules.
# La fonction doit retourner la liste de chaînes nettoyée.
#
# Testez avec `donnees = ['  Apple  ', '', 'Banana ', '   ', 'Orange']` et différentes options.
#
# 💡 Utilisez une boucle `for` et une nouvelle liste pour les résultats. Les méthodes `.strip()` et `.lower()` seront utiles.

def nettoyer_donnees(liste_chaines, supprimer_vides=True, convertir_minuscules=False):
    resultat = []
    for chaine in liste_chaines:
        propre = chaine.strip()
        if supprimer_vides and propre == "":
            continue
        if convertir_minuscules:
            propre = propre.lower()
        resultat.append(propre)
    return resultat


donnees = ['  Apple  ', '', 'Banana ', '   ', 'Orange']

print(nettoyer_donnees(donnees))
print(nettoyer_donnees(donnees, supprimer_vides=False))
print(nettoyer_donnees(donnees, convertir_minuscules=True))
print(nettoyer_donnees(donnees, supprimer_vides=False, convertir_minuscules=True))
