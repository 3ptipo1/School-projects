'''
Auteurs : DEPRES Adrien, GODET Jeanne, PETIT Gildas

Ce programme répond au cahier des charges de la première partie du 3ème projet
'''
import csv
import math
import random

def validation_croisee(characters):
    pass

def kNN(characters, character, k = 5):
    '''
    Fonction permettant de choisir la maison d'un profil donné
    à l'aide des profils existants en utilisant l'algorithme des
    k plus proches voisins. (en cas d'égalités : aléatoire)
    Paramètres :
        - characters : liste de dictionnaires contenants les informations
                        de chaque autres élèves
        - character : dictionnaire contenant le profil de l'élève à choisir
        - k = 5 : entier, par default à 5, indiquant le nombre de voisins
                    à considérer
    Sortie :
        - decision : (string) la maison choisie pour le candidat
        - neighbours : (list) Les k plus proches voisins du profil, ou les gens ayant les profils les plus similaires
    '''
    n = len(characters)
    distances = [[-1] for i in range(n)]
    mindset = ['Courage', 'Ambition', 'Intelligence', 'Good']
    traduction = {"Gryffindor":"Gryffondor","Ravenclaw":"Serdaigle","Hufflepuff":"Poufsouffle","Slytherin":"Serpentard"}
    for value in mindset:
        character[value] = int(character[value])

    for i in range(n):
        s = 0
        for value in mindset:
            characters[i][value] = int(characters[i][value])
            s += (character[value] - characters[i][value]) ** 2   
        distances[i] = [math.sqrt(s),characters[i]["House"], characters[i]["Name"]]
    distances.sort(key = lambda x:x[0])
    choice = {"Gryffindor":0, "Ravenclaw":0, "Hufflepuff":0, "Slytherin":0}
    neighbours = []
    for i in range(k):
        choice[distances[i][1]] += 1
        neighbours.append([distances[i][2],traduction[distances[i][1]]])
    m = 0
    decision = ""
    for house,count in choice.items():
        if count > m:
            m = count
            decision = house
    # pour partie 2 possible ajout des preferences de maisons pour departager
    #(comme Harry potter qui aurait pu aller a gryffondor ou serpentard mais
    # qui a demandé gryffondor au choixpeau)
        elif count == m: 
            m,decision = random.choice(((m,decision),(count,house)))
    decision = traduction[decision]
    return decision, neighbours
    






# import des persos et création, par jointure, de la table utilisée :
keys = ['Name', 'Courage', 'Ambition', 'Intelligence', 'Good', 'Gender', 'Job', 'House', 'Wand', 'Patronus', 'Species', 'Blood status', 'Hair colour', 'Eye colour', 'Loyalty', 'Skills', 'Birth', 'Death']

with open("Characters.csv", mode = "r", encoding = "utf-8") as f:
    text = csv.DictReader(f, delimiter=';')
    csv1 = [{key : value for key, value in element.items()} for element in text]

with open("Caracteristiques_des_persos.csv", mode = "r", encoding = "utf-8") as f:
    text = csv.DictReader(f, delimiter=';')
    csv2 = [{key : value for key, value in element.items()} for element in text]
    characters = [] 
    for element in csv2:
        for somebody in csv1:
            if element["Name"] == somebody["Name"]:
                characters.append(element)
                characters[-1].update(somebody)
                del characters[-1]["Id"]

# début du programme :               

def main():
    '''
    Procédure lançant le programme, l'IHM ...
    '''
    k = 5
    if input("Voulez vous choisir une valeur de k ? (y/n):") == "y":
        k = int(input("Rentrer votre valeur de k (entière et positive) :"))
    elif input("Voulez vous choisir la valeur de k à l'aide d'une validation croisée ? (y/n):") == "y":
        #k = validation_croisee(characters)
        pass

    moral_keys = ['Courage', 'Ambition', 'Intelligence', 'Good']
    if input("Voulez vous tester les cas d'exemples ? (y/n):") == "y":
        profiles = [{'Courage': 9, 'Ambition': 2, 'Intelligence':8, 'Good':9},
                    {'Courage': 6, 'Ambition': 7, 'Intelligence':9, 'Good':7},
                    {'Courage': 3, 'Ambition': 8, 'Intelligence':6, 'Good':3},
                    {'Courage': 2, 'Ambition': 3, 'Intelligence':7, 'Good':8},
                    {'Courage': 3, 'Ambition': 4, 'Intelligence':8, 'Good':8}]
        for profile in profiles:
            print("")
            print("Pour un élève ayant les caractéristiques suivantes :")
            for moral_key,value in profile.items():
                print(f"{moral_key} : {value}",end=" | ")
            print("")
            function_call = kNN(characters,profile,k)
            print(f"La maison que le choixpeau magique recommande pour ce profil est {function_call[0]} !")
            if input(f"Voulez vous voir les {k} plus proches voisins du profil ? (y/n):") == "y":
                print("Les élèves ressemblants le plus à ce profil sont :")
                for guy, house in function_call[1]:
                   print(f"- {guy} de la Maison {house}") 
            print("")
    else:
        character = dict()
        print("Entrez les valeurs pour :")
        for moral_key in moral_keys:
            character[moral_key] = ""
            while character[moral_key] == "":
                try :
                    character[moral_key] = int(input(f"- {moral_key} : "))
                    if character[moral_key] >= 10:
                        character[moral_key] = ""
                        raise "TRICHEUR"
                except :
                    print("Rentrez un nombre entier positif inférieur ou égal à 9 !")
        function_call = kNN(characters,character,k)
        print(f"La maison que le choixpeau magique recommande pour ce profil est {function_call[0]} !")
        if input(f"Voulez vous voir les {k} plus proches voisins du profil ? (y/n):") == "y":
                print("Les élèves ressemblants le plus à ce profil sont :")
                for guy, house in function_call[1]:
                   print(f"- {guy} de la Maison {house}") 
    if input("Voulez vous continuer ? (y/n):") == "y":
        main()
    else:
        return None

main()
