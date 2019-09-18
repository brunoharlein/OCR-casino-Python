from random import randrange #import de la fonction randrange du module import pour faire du random number
from math import ceil #import de la fonction ceil du module math pour arrondir et ne pas obtenir de float

argentDepart = 1000 #somme de départ

print("Début de la partie vous avez", argentDepart) #Début de partie avec 1000

while 1: #tant que 1 est True
    nombreMise = -1 #nombre pour la mise valeur de départ en erreur
    while nombreMise < 0 or nombreMise > 49:
        nombreMise = input("miser entre 0 et 49")
        try:
            nombreMise = int(nombreMise) #conversion en integer
        except ValueError:
            print("il faut entrer un nombre entre 0 et 49")
            nombreMise = -1 #erreur pour que la boucle se face
            continue #pour ne pas planter le programme malgré les erreurs de nombres

        if nombreMise < 0:
            print("entrer un nombre plus grand que 0")

        if nombreMise > 49:
            print("Votre nombre est trop grand")

    argentMise = 0
    while argentMise <= 0 or argentMise > argentDepart:
        argentMise = input("la somme que vous voulez mettre")
        try:
            argentMise = int(argentMise)
        except ValueError:
            print("La somme que vous voulez mettre")
            argentMise = -1
            continue

        if argentMise < 0:
            print("la somme doit etre superieur à 0")

        if argentMise > argentDepart:
            print("impossible de mettre plus que ce que vous avez il vous reste,", argentDepart)

    nombreGagnant = randrange(50) #prendre en random entre 0 et 50 pour la variable nombreGagnant
    print("le numero est", nombreGagnant )
    if nombreGagnant == nombreMise: # si le nombreGagnat est égal au nombreMise
        print("Bravo !! vous gagnez : ", argentMise * 3) #affichage du total de la somme
        argentDepart += argentMise * 3 #ajout des gains dans argentDépart

    elif nombreGagnant % 2 == nombreMise % 2: #si nombreGagnant et nombreMise sont pair
        argentMise = ceil(argentMise * 0.5) # arrondi de argentMise
        print("La couleur est bonne voici : ", argentMise)
        argentDepart += argentMise #ajout des gains dans argentDepart

    else:
        print("pas de chance")
        argentDepart -= argentMise #soustraction des gains dans argentDepart

    if argentDepart <= 0:
        print("c'est la fin il n'y a plus d'argent")
        break # Si argentDepart est inferieur ou egal à 0 la boucle se ferme

    else:
        print("vous avez", argentDepart)
        fin = input("pour quitter taper oui")
        if fin == "oui":
            print("au revoir")
            break # Si le joueur tape oui à la fin de son tour il quitte la partie



