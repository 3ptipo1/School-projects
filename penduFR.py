def levraijeu():
    '''
    Argument : Rien
    Sortie : Rien
    Cette fonction permet de jouer une partie de pendu avec plusieurs
    paramètres customisables comme: le nombre d'erreur, le choix des mots
    ou la possibilité de tenter de guess le mot en entier
    '''
    mots = ["intergouvernementalisations", "chaussette",
            "nsi", "wagon", "kepi", "gargouillis", "mystere"]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                "j", "k", "l", "m", "n", "o", "p", "q", "r",
                "s", "t", "u", "v", "w", "x", "y", "z"]
    te = input("Souhaitez vous jouer avec un mot de votre choix ? (o/n): ")
    if te == "o":
        but = input("Rentrez votre mot : ").lower().strip()
        # on peut choisir un mot custom
    else:
        but = random.choice(mots)   # ou un mot de la liste de départ
    vf = True                       # booleen de réussite
    n = len(but)
    vu = [0] * n         # liste qui indique quelles lettres sont découvertes 
    somme = 0            # conpteur pour savoir quand le mot sera découvert
    ban = set()
    nberreur = int(input("Avec combien d'erreurs "\
                         "possibles souhaitez vous jouer ? : "))
    while vf:
        print("")
        print("")
        print("Votre mot est : ", end="")
        for i in range(n):   # on affiche que les lettres découvertes
            if vu[i] == 1:
                print(but[i], end="")
            else: 
                print("_", end="")
        print("")
        print("Les lettres bannies sont", end=" ")
        for i in ban:
            print(i, end=" ")
        print("")
        print("et le nombre de fautes que vous pouvez faire est", nberreur)
        l = input("Veuillez choisir une lettre "\
                  "ou tenter de deviner le mot en entier : ").lower()
                # .lower() permet de supprimer les majuscules d'un string
                # au cas où l'utilisateur se soit trompé 
        if len(l) > 1: # cas où l'utilisateur a tenté de guess le mot en entier
            if l == but:
                vf = False
            else:
                print("Vous vous êtes trompé !")
                nberreur -= 1
                if nberreur == 0:
                    print("Vous avez épuisé toutes vos chances !")
                    print("Le mot mystère était", but)
                    return 42;
        else:
            if l not in alphabet: 
                # message renvoyé en cas d'invalidité du résultat
                print("Quand on joue à un jeu, "\
                      "il faut en respecter les règles")
                continue
            if l in ban:    # message renvoyé en cas de lettre déjà utilisée
                print("Vous avez déjà essayé cette lettre !")
                continue
            if l in but:    # message de lettre juste
                print("La lettre choisie se trouve dans le mot")
                for i in range(n):
                    if but[i] == l:
                        vu[i] = 1
                        somme += 1
                if somme == n:
                    vf = False
            else:
                print("Vous vous êtes trompé !")
                nberreur -= 1
                if nberreur == 0:
                    print("Vous avez épuisé toutes vos chances !")
                    print("Le mot mystère était", but)
                    return 42
            ban.add(l)  # .add() permet d'ajouter des éléments à un set,
            # ici pour ajouter des lettres au set des lettres déjà utilisées
    print("Bravo ! vous avez trouvé le mot mystere :", but)
    
levraijeu()
