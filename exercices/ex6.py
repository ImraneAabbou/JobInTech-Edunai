# Créez une variable de mois avec la valeur 'janvier'
# Utilisez des f-strings et des méthodes de chaînes pour créer un en-tête : '===== RAPPORT DES VENTES - JANVIER ====='
# Affichez l'en-tête

# 💡 Combinez f-strings, .upper(), et la multiplication de chaînes ('=' * 5)

mois = 'janvier'
header = f"{'=' * 5} RAPPORT DES VENTES - {mois.upper()} {'=' * 5}"

print(header)
