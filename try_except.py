# Récupération d'erreurs dont le type est inconnu

try:
    # bout de code qui génère une erreur
    pass
except Exception as error:
    print(f"Une erreur est survenue : {error}")


# Récupération d'erreurs dont le type est connu

try:
    # bout de code qui génère une erreur
    pass
except ValueError as error:
    print(f"Une erreur de type ValueError est survenue : {error}")


# Récupération d'erreurs multiples

try:
    # bout de code qui génère une erreur
    pass
except ValueError as error:
    print(f"Une erreur est survenue : {error}")
except KeyError as kerror:
    print(f'Une erreur de type kerror est survenue : {kerror}')


# Récupération d'erreurs multiples avec un seul bloc except

try:
    # bout de code qui génère une erreur
    pass
except (ValueError, KeyError) as error:
    print(f"Une erreur est survenue : {error}")


# Récupération d'erreurs multiples avec un filet de sécurité

try:
    # bout de code qui génère une erreur
    pass
except (ValueError, KeyError) as error:
    print(f"Une erreur est survenue : {error}")
except Exception as error:
    # Ce bloc est exécuté si une erreur non prévue survient
    print(f"Une erreur inconnue est survenue : {error}")


# Utilisation de l'instruction finally

try:
    # bout de code qui génère une erreur
    pass
except (ValueError, KeyError) as error:
    print(f"Une erreur est survenue : {error}")
finally:
    print("Le bloc try/except est terminé")


# Utilisation de l'instruction else

try:
    # bout de code qui génère une erreur
    pass
except (ValueError, KeyError) as error:
    print(f"Une erreur est survenue : {error}")
else:
    print("Le bloc try est terminé sans erreur")
