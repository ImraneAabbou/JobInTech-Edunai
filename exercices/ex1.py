investissement = 1000
taux_interet = .05
duree = 3

interet_compose = investissement * (1 + taux_interet) ** duree

interet_gagnee = interet_compose - investissement

print(
        "investissement: ", investissement, "\n",
        "interet_compose: ", interet_compose, "\n",
        "interet_gagnee: ", interet_gagnee, "\n",
        sep=""
    )
