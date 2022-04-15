# coding: utf-8
"""
Auteurs : DEPRES Adrien, GODET Jeanne, PETIT Gildas

Ce programme répond au cahier des charges de la deuxième partie du 3ème projet
et rend la page HTML dynamique
"""
from browser import document, html, timer
from kNN_revisite import kNN, purge, test_equilibrage
import csv


def page_resultat(maison, voisins):
    """
    Procédure affichant le résultat du quizz : la maison, les voisins
    et leurs maisons ainsi qu'une image de la maison
    Entrées :
        - maison : (str) le nom de la maison
        - voisins : liste contenant pour les k premiers voisins,
                        leur nom et leur maison.
    """
    document["zone_interaction"].textContent = ""
    document["zone_interaction"] <= html.H1("Annonce du choix !")

    document["zone_interaction"] <= html.H2("Votre maison sera :")
    document["zone_interaction"] <= html.CENTER(
        html.B(maison + " !", style="color:rgb(150, 10, 10);")
    ) + html.BR() + html.BR()
    # mettre une image en fonction de la maison :
    if maison == "Serpentard":
        document["zone_image"].clear()
        document["zone_image"] <= html.IMG(
            src="https://lecahier.com/wp-content/uploads/2021/07/226-2269266_slytherin-crest-png-harry-potter-slytherin-logo.png",
            alt="Image_Serp",
            height=300,
        )
    elif maison == "Poufsouffle":
        document["zone_image"].clear()
        document["zone_image"] <= html.IMG(
            src="https://d1v224g40dbxxy.cloudfront.net/s3fs-public/gallery-images/Huffle_0.png?VersionId=lPf6cPdBB2rMbdHm9oZM0w0iJx07hoej",
            alt="Image_Serp",
            height=300,
        )
    elif maison == "Gryffondor":
        document["zone_image"].clear()
        document["zone_image"] <= html.IMG(
            src="https://cdn141.picsart.com/320281721278211.png",
            alt="Image_Serp",
            height=300,
        )
    else:
        document["zone_image"].clear()
        document["zone_image"] <= html.IMG(
            src="https://nsa40.casimages.com/img/2019/09/02/190902115623988868.png",
            alt="Image_Serp",
            height=300,
        )

    document["zone_interaction"] <= (html.B("Vos voisins sont :") 
                                        + html.BR() + html.BR())
    for eleve in voisins:
        document["zone_interaction"] <= (
            "- "
            + html.B(eleve[0])
            + " de la Maison "
            + html.B(TRAD[eleve[1]])
            + html.BR()
        )

    document["zone_interaction"] <= html.BR() + html.BUTTON(
        "Cliquez pour refaire le quizz ",
        Class="button button2",
        onclick="location.reload();",
    )


def page_transition():
    """
    Procédure permettant de calculer le profil et d'appliquer
    l'algorithme des k plus proche voisins.
    Elle affiche aussi une page donnant un choix à l'utilisateur en cas
    d'égalité entre deux maisons.
    """
    document["zone_progression"].style.display = "none"
    profil = [0] * 4
    nb_stat_par_car = [0] * 4
    for stats in moyenne:
        for i in range(4):
            if stats[i] != -1:
                profil[i] += stats[i]
                nb_stat_par_car[i] += 1
    for i in range(4):
        profil[i] = profil[i] // nb_stat_par_car[i]
    character = {
        "Courage": profil[0],
        "Ambition": profil[1],
        "Intelligence": profil[2],
        "Good": profil[3],
    }
    decision, voisins = kNN(purge(characters), character, 5)
    if len(decision) != 1:
        document["zone_interaction"].textContent = ""
        document["zone_interaction"] <= html.CENTER(
            html.H1("Le Choixpeau se questionne :")
        )
        for laquelle in range(len(decision)):
            doute = decision[laquelle]
            document["zone_interaction"] <= html.BUTTON(
                TRAD[doute] + " ?",
                id="doute" + str(laquelle + 1),
                Class="button button2",
                value=laquelle,
            ) + html.BR() + html.BR()
            document["doute" + str(laquelle + 1)].bind(
                "click",
                lambda x: page_resultat(
                    TRAD[decision[int(x.target.value)]],voisins),
            )
    else:
        page_resultat(TRAD[decision[0]], voisins)


def update_quizz(event):
    """
    Procédure qui rend les eléments du quizz intéractifs et qui permet
    de terminer la phase d'acquisition de donnée après la dernière question
    Entrée:
        -event  : contient toute les infos lié au click
                    (ici "target.value")
    """
    stats = []
    n_question = int(document["zone_question"].attrs["value"])
    CARACTERISTIQUES = ["Courage", "Ambition", "Intelligence", "Good"]
    for clef in CARACTERISTIQUES:
        stats.append(faq[n_question]["reponse" + event.target.value][clef])
    moyenne.append(stats)
    n_question += 1
    if n_question < len(faq):
        document["zone_question"].textContent = faq[n_question]["question"]
        document["zone_question"].attrs["value"] = str(n_question)
        document["progression"].attrs["value"] = str(n_question + 1)
        for i in range(3):
            document["bouton" + str(i + 1)].textContent = faq[n_question][
                "reponse" + str(i + 1)
            ]["reponse"]
    else:
        page_transition()


def quizz(event):
    """
    Procédure qui met en place les éléments intéractifs nécessaires au quizz
    Entrée :
        -event : contient toute les infos lié au click (ici inutile)
    """
    global click_bouton_reponse
    document["zone_progression"].style.display = "block"
    document["zone_interaction"].textContent = ""
    document["zone_interaction"] <= html.CENTER(html.H1("Passons au quizz !"))
    document["zone_interaction"] <= html.H2(
        faq[0]["question"], id="zone_question", value=0
    )
    for i in range(3):
        document["zone_interaction"] <= html.BUTTON(
            faq[0]["reponse" + str(i + 1)]["reponse"],
            id="bouton" + str(i + 1),
            Class="button button2",
            value=i + 1,
        ) + html.BR()
        document["bouton" + str(i + 1)].bind("click", update_quizz)


def initial():
    """
    Procédure rendant le contenu de la page HTML de départ dynamique
    Actuellement inutile / projet possible de bonus --> modularité
    """
    document["bouton_debut"].bind("click", quizz)


# création des structures de données et ouverture des fichiers nécéssaires

characters = []
moyenne = []


with open("table_question.csv", mode="r", encoding="utf-8") as f:
    reader = f.readlines()
    faq = []
    for ligne in reader:
        ligne = ligne.replace("\xa0", " ")
        question, *reponses = tuple(ligne.strip().split(";"))
        faq.append({"question": question})
        for i in range(3):
            reponse, profil = reponses[i].split("|")
            cou, amb, it, good = map(int, profil.split("/"))
            faq[-1]["reponse" + str(i + 1)] = {
                "reponse": reponse,
                "Courage": cou,
                "Ambition": amb,
                "Intelligence": it,
                "Good": good,
            }

with open("Characters.csv", mode="r", encoding="utf-8") as f:
    text = csv.DictReader(f, delimiter=";")
    csv1 = [{key: value for key, value in element.items()} for element in text]

with open("Caracteristiques_des_persos.csv", mode="r", encoding="utf-8") as f:
    text = csv.DictReader(f, delimiter=";")
    csv2 = [{key: value for key, value in element.items()} for element in text]
    characters = []
    for element in csv2:
        for somebody in csv1:
            if element["Name"] == somebody["Name"]:
                characters.append(element)
                characters[-1].update(somebody)
                del characters[-1]["Id"]

TRAD = {
    "Gryffindor": "Gryffondor",
    "Ravenclaw": "Serdaigle",
    "Hufflepuff": "Poufsouffle",
    "Slytherin": "Serpentard",
}

initial()
# test_equilibrage(faq, characters) # pour tester
