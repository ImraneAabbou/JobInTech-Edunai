# Créez des listes pour adresses_livraison ['123 Rue Main', '456 Ave Oak', '789 Rd Pine', '321 Rue Elm'], distances_km [2.5, 4.2, 1.8, 3.6], temps_livraison [15, 25, 12, 20], et poids_colis [2.1, 4.5, 1.2, 3.8]
# Calculez l'efficacité de livraison (colis par minute) pour chaque arrêt
# Triez les livraisons par distance (la plus courte en premier) pour l'optimisation d'itinéraire
# Calculez la distance totale de l'itinéraire et le temps total estimé
# Identifiez l'arrêt de livraison le plus efficace (temps le plus court par km)

adresses_livraison = ["123 Rue Main", "456 Ave Oak", "789 Rd Pine", "321 Rue Elm"]
distances_km = [2.5, 4.2, 1.8, 3.6]
temps_livraison = [15, 25, 12, 20]
poids_colis = [2.1, 4.5, 1.2, 3.8]


info_zipped = list(zip(adresses_livraison, distances_km, temps_livraison, poids_colis))

for i in info_zipped:
    print(f"{i[0]}:", i[3] / i[2], "kg/h")

print("livraisons trier par distances:", sorted(info_zipped, key=lambda i: i[1]))

print(
    f"total distance de {sum(distances_km)} km; ",
    f"tout sera delivree apres {sum(temps_livraison)} h"
)

print("livraison le plus efficace:", min(info_zipped, key=lambda i: i[2] / i[1]))
