#     Créez deux sets de noms d'employés, un pour les 'Ventes' et un pour le 'Marketing'.
#     Trouvez les employés qui sont dans les deux départements (intersection).
#     Trouvez tous les employés uniques des deux départements (union).
#
# 💡 Utilisez `ventes.intersection(marketing)` et `ventes.union(marketing)`.


employes_ventes = {
    "someone 1",
    "someone 5",
    "someone 9",
    "someone 0",
    "someone 3",
}

employes_marketing = {
    "someone 5",
    "someone 8",
    "someone 2",
    "someone 3",
}

print("intersection employes:", employes_marketing.intersection(employes_ventes))
print("union employes:", employes_marketing.union(employes_ventes))
