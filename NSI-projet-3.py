'''
'''
import csv
import math


def validation_croisee():
    pass

def kNN(characters, character, k = 5):
    n = len(characters)
    distances = [-1 for _ in n]
    mindset = ['Courage', 'Ambition', 'Intelligence', 'Good']

    for i in range(n):
        s = 0
        for value in mindset:
            s += (character[value] - characters[i][value]) ** i   
        distances[i] = math.sqrt(s)
    






# import des persos et création, par jointure, de la table utilisée
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

# début du programme                
