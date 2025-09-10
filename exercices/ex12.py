# Convertir 5 miles en kilomètres (1 mile = 1.609 km)
# Convertir 10 kg en livres (1 kg = 2.205 lbs)
# Convertir 32°F en Celsius avec la formule : (F - 32) × 5/9


distance_km = 10
distance_mile= distance_km / 1.609

poids_kg = 20
poids_lbs = poids_kg / 2.205

tmp_f = 25
tmp_c = (tmp_f - 32) * 5/9

print(
        f"{distance_km} km = {distance_mile} mile", "\n",
        f"{poids_kg} kg = {poids_lbs} lbs", "\n",
        f"{tmp_f} F = {tmp_c} C", "\n",
        sep=""
    )
