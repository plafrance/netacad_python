# Ceci est un commentaire

# Et maintenant l'affectation d'une variable de type entier
âge = 23

# l'affectation d'une variable de type chaîne de caractères
nom = "Gaston"

# une variable booléenne indiquant la validité de la réponse
valide = False

# Boucle tant que la réponse n'est pas satisfaisante
while not valide:

    # Une saisie au clavier
    réponse = input("Désirez-vous savoir l'âge de " + nom + " ?")

    # on transpose en minuscules
    réponse = réponse.lower()

    # une action conditionnelle :
    if réponse == "oui" or réponse == "o":
        # Affichage incluant le transtypage d'un entier en chaîne de caractères
        print(nom + " est âgé de " + str(âge))
        valide = True
    # si les 3 premiers caractères de réponse correspondent à «non»
    elif réponse[0:3] == "non":
        print("Tant pis")
        valide = True
    else:
        print("Je n'ai pas compris votre réponse. Laissez-moi vour poser la question de nouveau.")
