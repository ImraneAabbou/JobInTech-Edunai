# Créez une liste de points de fidélité [850, 1200, 750, 1500, 920, 1100]
# Triez les clients par points (du plus élevé au plus bas)
# Identifiez les 3 meilleurs clients (top 3)

points_fidelite = [850, 1200, 750, 1500, 920, 1100]

points_fidelite.sort()

high_fidelity_points = points_fidelite[:3]

print(high_fidelity_points)
