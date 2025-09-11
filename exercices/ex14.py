# Commencez avec une chaîne CSV : 'Jean Dupont,Ventes,55000'
# Utilisez la méthode .split(',') pour diviser la chaîne en une liste
# Extrayez le nom, le département et le salaire de la liste
# Affichez chaque information avec une étiquette claire

# 💡 .split(',') crée une liste, vous pouvez ensuite accéder aux éléments avec [0], [1], etc.


csv_string = 'Jean Dupont,Ventes,55000'
data = csv_string.split(',')

fullname = data[0]
departement = data[1]
salary = data[2]

print(f"""
nom complet: {fullname}
departement: {departement}
salaire: {salary}
""")
