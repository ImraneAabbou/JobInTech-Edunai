# Commencez avec une chaîne de données désordonnée comme 'ID:123; Nom : Jean Dupont; Tél: 555.123.4567 '
# Nettoyez les espaces de début/fin
# Remplacez les points dans le numéro de téléphone par des tirets
# Séparez la chaîne en parties logiques en utilisant `.split(';')`

raw_data = "ID:123; Nom : Jean Dupont; Tél: 555.123.4567 "

raw_data = raw_data.strip() # netoyage des espaces

raw_data = raw_data.replace(".", "-") # remplacement des point avec tiret

data = raw_data.split("; ")

print(f"""
{data[0]}
{data[1]}
{data[2]}
""")

