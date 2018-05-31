import requests

session = requests.session()

# r = session.get('localhost', port=5000)

réponse = session.post('http://localhost:5000/login', data={"username": "Bob"})

while True:
    page = réponse.text
    opérande1 = page.find('+')-3
    opérande2 = page.find('+')+2

    if opérande1 < 0:
        print(réponse.text)
        break

    opérande1 = int(page[opérande1:opérande1+2])
    opérande2 = int(page[opérande2:opérande2+2])

    somme = str(opérande1+opérande2)
    #print(opérande1, opérande2, réponse)
    réponse = session.post('http://localhost:5000/quiz',
                           data={"reponse": somme})
