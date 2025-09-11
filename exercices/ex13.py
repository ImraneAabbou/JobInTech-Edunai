# Prenez le prénom, le nom de famille et l'année d'embauche d'un employé comme variables
# Créez un ID d'employé en utilisant les 3 premières lettres du nom de famille (en majuscules), les 2 premières lettres du prénom (en majuscules), et l'année
# Combinez-les avec un tiret : 'DUPJE-2024' pour Jean Dupont, embauché en 2024

prenom = "jean"
nom = "dupdont"
date_emboche = "2024-03-03"

id1 = nom[:3].upper()
id2 = prenom[:2].upper()
year_daumboche = date_emboche.split('-')[0]
identifier = f"{id1}{id2}-{year_daumboche}"

print(f"id de {prenom} {nom} est :", identifier)
