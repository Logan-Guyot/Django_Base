from django.shortcuts import redirect

# crée ses middleware si besoin
# sert pour les vérification des requete ( d'autantification par exemple )

class MiddlewarePersonalyser:
    def __init__(self, get_response):
        self.get_response = get_response
        # mettre les condition ici