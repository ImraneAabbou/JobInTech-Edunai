#     Créez deux sets d'ID clients. Un pour les 'acheteurs_mois_dernier' et un pour les 'abonnes_newsletter'.
#     Trouvez les clients qui ont acheté le mois dernier ET qui sont abonnés à la newsletter.
#     Trouvez les clients qui sont abonnés mais qui n'ont PAS acheté le mois dernier.
#     Trouvez tous les clients uniques des deux groupes.
#
# 💡 Utilisez les opérations sur les sets : `intersection`, `difference`, et `union`.

acheteurs_mois_dernier = {"client 1", "client 4", "client 9"}
abonnes_newsletter = {"client 2", "client 3", "client 7"}


abonne_pas_achete = abonnes_newsletter.difference(acheteurs_mois_dernier)
abonne_et_achete = abonnes_newsletter.intersection(acheteurs_mois_dernier)
tous_uniq = abonnes_newsletter.union(acheteurs_mois_dernier)

print("abonne et achete:", abonne_et_achete)
print("abonne pas achete:", abonne_pas_achete)
print("tous les clients:", tous_uniq)
