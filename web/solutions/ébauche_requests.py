# Nécessite l'installation du module requests
#
# Sur Linux :
# sudo pip install requests
#
# Sur Windows :
# pip install requests

import requests

url_base = "http://csir.dept-info.crosemont.quebec:5000"

# Crée la session
session = requests.session()

# Inscrit l'utilisateur en envoyant le contenu du formulaire par un POST
réponse = session.post(url_base + "/login",
                       data={"username": "nom d'utilisateur"})

while True:
    # Lit le contenu de la réponse
    html = réponse.text

    # Trouver la réponse ici
    somme = ???

    # Envoie le formulaire contenant réponse
    réponse = session.post(url_base + "/quiz", data={"reponse": somme})
