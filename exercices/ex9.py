# Étant donné un `message_utilisateur`, s'il contient le mot 'aide', affichez 'Comment puis-je vous aider ?'. Sinon, affichez 'Je ne comprends pas'.
message_utilisateur = "peux-tu m'aider avec ma commande ?"
reponse = ""

if "aide" in message_utilisateur:
    reponse = "Comment puis-je vous aider ?"
else:
    reponse = "Je ne comprends pas"

print(reponse)
