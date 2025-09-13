#    Créez une liste de revenus trimestriels [125000, 138000, 142000, 156000]
#    Calculez la croissance entre chaque trimestre
#    Identifiez le trimestre avec la plus forte croissance


revenus_trimestriels = [125000, 138000, 142000, 156000]

croissances = list(
    map(
        lambda pair: pair[1] - pair[0],
        zip(revenus_trimestriels, revenus_trimestriels[1:])
    )
)


print(
    "croissances: ", croissances, "\n",
    "max croissance: ", max(croissances), "\n",
    sep=""
)
