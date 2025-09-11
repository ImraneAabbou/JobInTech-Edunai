# Commencez avec un titre de blog comme 'Ma Première Journée dans une Entreprise Tech !'
# Convertissez le titre en minuscules
# Remplacez les espaces par des tirets
# Supprimez les caractères spéciaux (comme '!') pour créer un slug propre : 'ma-premiere-journee-dans-une-entreprise-tech'

# 💡 Enchaînez `.lower()`, `.replace(' ', '-')`, et `.replace('!', '')`


title = 'Ma Première Journée dans une Entreprise Tech !'
slug = title.replace("!", "").strip().replace(" ", "-").lower()

print("slug propre:", slug)
