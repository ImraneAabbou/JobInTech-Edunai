#    Créez une liste de quantités en stock [45, 23, 67, 12, 89, 34, 56]
#    Identifiez les produits avec un stock faible (moins de 30 unités)
#    Calculez le stock total et le stock moyen
# 💡 Utilisez une boucle ou une compréhension de liste pour filtrer

stock = [45, 23, 67, 12, 89, 34, 56]

stock_faible = list(filter(lambda x: x < 30, stock))

stock_total = sum(stock)

stock_avg = stock_total / len(stock)

print(
    "stock faible: ", stock_faible, "\n",
    "stock total: ", stock_total, "\n",
    "stock avg: ", stock_avg, "\n",
    sep=""
)
