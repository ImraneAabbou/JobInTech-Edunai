#     Étant donné un `revenu`, calculez l'impôt : 10% pour un revenu jusqu'à 50k€, 20% pour 50k€-100k€, et 30% pour plus de 100k€.
#
# 💡 C'est un excellent cas d'utilisation pour `if/elif/else`.


revenu = 5000

impot_perc_dict = {
    "a": 0.3,
    "b": 0.2,
    "c": 0.1,
}

impot_perc = 0

if revenu <= 50000:
    impot_perc = impot_perc_dict["c"]
elif revenu <= 100000:
    impot_perc = impot_perc_dict["b"]
else:
    impot_perc = impot_perc_dict["a"]

impot = revenu * (1 + impot_perc)


print("impot:", impot)
