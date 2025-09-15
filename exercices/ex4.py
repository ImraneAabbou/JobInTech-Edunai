#     Créez une liste d'adresses IP de visiteurs avec des doublons : ['ip1', 'ip2', 'ip1', 'ip3', 'ip2'].
#     Convertissez la liste en un set pour trouver les adresses IP uniques.
#     Affichez le nombre de visiteurs uniques en utilisant `len()` sur le set.
#
# 💡 Utilisez `set(ma_liste)` pour convertir une liste en set et supprimer les doublons.


ips = ['ip1', 'ip2', 'ip1', 'ip3', 'ip2']

ips_unique = set(ips)

print('nombre visiteurs:', len(ips_unique))
