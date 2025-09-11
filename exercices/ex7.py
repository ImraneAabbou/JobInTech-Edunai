# Commencez avec l'email 'jean.dupont@exemple.com'
# Trouvez la position du symbole '@'
# Extrayez la partie de la chaîne avant le '@' et affichez-la

# 💡 Utilisez la méthode .index('@') pour trouver la position, puis découpez la chaîne

email = 'jean.dupont@exemple.com'
arobask_position = email.index('@')
username = email[:arobask_position]

print("la partie de la chaîne avant le '@':", username)
