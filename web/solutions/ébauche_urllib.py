import urllib.request

url_base = "http://csir.dept-info.crosemont.quebec:5000"

# Crée une session
req = urllib.request.Request(url_base)

# ouvre l'URL
réponse = urllib.request.urlopen(req)

# Conserve le cookie
cookie = réponse.headers.get("Set-Cookie")

# Envoie une requête avec le nom d'utilisateur
req = urllib.request.Request(url_base + "/login", data=b"username=Bob")

# Place le cookie avec la requête
req.headers["Cookie"] = cookie

# Envoie la requête
réponse = urllib.request.urlopen(req)

compte = 0
while True:
    print(compte)
    # Récupére le cookie de la réponse
    cookie = réponse.headers.get("Set-Cookie")
    # Lit le contenu de la réponse
    html = str(réponse.read())

    # Trouver la réponse ici
    somme = ???

    # Encode la réponse en ascii
    data = ("reponse="+somme).encode("ascii")

    # Crée la nouvelle requête
    req = urllib.request.Request(url_base + "/quiz", data=data)
    req.headers["Cookie"] = cookie

    # Envoie la requête
    réponse = urllib.request.urlopen(req)
    compte += 1
