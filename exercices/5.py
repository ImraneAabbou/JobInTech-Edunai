# Créez une classe `UtilisateurSiteWeb`.
#     Ajoutez une variable de classe `nombre_utilisateurs = 0`.
#     Dans la méthode `__init__`, incrémentez `nombre_utilisateurs` de 1 chaque fois qu'un nouvel utilisateur est créé.
#
# Créez trois objets `UtilisateurSiteWeb` puis imprimez `UtilisateurSiteWeb.nombre_utilisateurs` pour voir le total.
#
# 💡 Les variables de classe sont définies directement dans la classe, pas dans une méthode. Accédez-y avec `UtilisateurSiteWeb.nombre_utilisateurs`.


class UtilisateurSiteWeb:
    nombre_utilisateurs = 0

    def __init__(self):
        UtilisateurSiteWeb.nombre_utilisateurs += 1


u1 = UtilisateurSiteWeb()
u2 = UtilisateurSiteWeb()

print("total d'utilisateur:", UtilisateurSiteWeb.nombre_utilisateurs)
