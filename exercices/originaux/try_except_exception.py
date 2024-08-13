# Créer une exception NotLoggedIn et la raise si l'utilisateur n'est pas logged-in

def test_loggin(user: dict):
    if user.pwd != "toto":
        # raise NotLoggedIn
        pass
    return 1
