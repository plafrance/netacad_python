import urllib.request

# Crée une session
req = urllib.request.Request(
    'http://csir.dept-info.crosemont.quebec:5000')

# ouvre l'URL
réponse = urllib.request.urlopen(req)

# Conserve le cookie
cookie = réponse.headers.get('Set-Cookie')

# Envoie une requête avec le nom d'utilisateur
req = urllib.request.Request(
    'http://csir.dept-info.crosemont.quebec:5000/login', data=b"username=Bob")

# Place le cookie avec la requête
req.headers['Cookie'] = cookie

# Envoie la requête
réponse = urllib.request.urlopen(req)

compte = 0
while True:
    print(compte)
    # Récupére le cookie de la réponse
    cookie = réponse.headers.get('Set-Cookie')
    # Lit le contenu de la réponse
    html = str(réponse.read())

    opérande1 = html.find('+')-3
    opérande2 = html.find('+')+2

    if opérande1 < 0:
        print(html)
        break

    opérande1 = int(html[opérande1:opérande1+2])
    opérande2 = int(html[opérande2:opérande2+2])

    somme = str(opérande1+opérande2)

    # Encode la réponse en ascii
    data = ("reponse="+somme).encode('ascii')

    # Crée la nouvelle requête
    req = urllib.request.Request(
        'http://csir.dept-info.crosemont.quebec:5000/quiz', data=data)
    req.headers['Cookie'] = cookie

    # Envoie la requête
    réponse = urllib.request.urlopen(req)
    compte += 1
