#     Stockez la configuration d'un serveur dans un tuple : ('192.168.1.1', 8080, 'production').
#     Accédez à l'adresse IP (le premier élément) et affichez-la.
#     Essayez de changer le numéro de port et observez l'erreur (car les tuples sont immuables).
#
# 💡 Accédez aux éléments avec l'indexation `config[0]`, mais vous ne pouvez pas assigner une nouvelle valeur.

server = ("192.168.1.1", 8080, "production")

(ip, *_) = server

print("ip:", ip)

server[1] = 4444  # err
