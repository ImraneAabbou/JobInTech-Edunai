# Si la `temperature` est inférieure à 0°C OU si `il_pleut` est `True`, affichez 'Restez à l'intérieur !'. Sinon, affichez 'Profitez du beau temps'.
temperature = -3
il_pleut = False
message = ""

if temperature < 0 or il_pleut:
    message = "Restez à l'intérieur !"
else:
    message = "Profitez du beau temps"

print(message)
