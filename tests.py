#Rozhina Mousavi
#TP3
#25 octobre 2022
import random

#variable numero_combat est egale a 0
numero_combat = 0

#variable nombres_de_victoires est egale a 0
nombres_de_victoires = 0

#variable nombres_de_defaites est egale a 0
nombres_de_defaites = 0

#variable autre_partie est egale a la lettre o
autre_partie = "o"

#variable minimum est egale a 1
minimum = 1

#variable maximum est egale a 12
maximum = 12

#fonction nouveau_niveau_vie qui change definit si la partie est victoire ou une defaite et definit le niveau de vie de l'utiliusateur selon si le score du de final de l"utilisateur est plus petit ou egal ou plus grand que la force de l'adversaire
def nouveau_niveau_vie():
    global niveau_vie
    #si score du de final est plus petit ou egal a la force de l'adversaire le variable c
    if score_dé_final <= force_adversaire:
        global combat_statut
        combat_statut = "defaite"
#
        niveau_vie -= int(force_adversaire)

    elif score_dé_final > force_adversaire:
        combat_statut = "victoire"

        niveau_vie += int(force_adversaire)

#fonction gange_perdu qui definit le nombres de victoires pour le nombre de victoires consecutifs
def gange_perdu():
    global nombres_de_victoires
    global nombres_de_defaites
    if combat_statut == "victoire":
        nombres_de_victoires += 1
    elif combat_statut == "defaite":
        nombres_de_victoires = 0


def augmentation():
    if nombres_de_victoires > 3:
        global minimum
        global maximum
        minimum +=5
        maximum +=5
    elif nombres_de_victoires < 3:
        minimum = 1
        maximum = 12


def combat():
    global numero_combat
    numero_combat += 1


def contourner_monstre():
    global niveau_vie
    niveau_vie -= 1





def instructions():
    print("""Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. 
Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  
Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.

La partie se termine lorsque les points de vie de l’usager tombent sous 0.

L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie. """)


def statut_partie():
    print("Adversaire: " + str(numero_adversaire))
    print("Force de l'adversaire: " + str(force_adversaire))
    print("Niveau de vie de l'usager: " + str(niveau_vie))
    print("Combat " + str(numero_combat) + ": " + str(nombres_de_victoires) + " victoires vs " + str(
        nombres_de_defaites) + " defaites")


def jeu():
    boucle_jeu = True
    while boucle_jeu:
        global force_adversaire
        force_adversaire = random.randint(minimum,maximum)
        global score_dé_1
        global score_dé_2
        global score_dé_final
        score_dé_1 = random.randint(1, 6)
        score_dé_2 = random.randint(1, 6)
        score_dé_final = score_dé_1 + score_dé_2
        print(score_dé_1)
        print(score_dé_2)
        print(score_dé_final)
        global numero_adversaire
        numero_adversaire = random.randint(1, 100)
        print("Vous tombez face à face avec un adversaire de difficulté:" + str(force_adversaire))

        quoi_faire = ("""Que voulez-vous faire? 
            1- Combattre cet adversaire
            2- Contourner cet adversaire et aller ouvrir un autre porte
            3- Afficher les règles du jeu
            4- Quitter la partie
            *Entrer le numero de l'option choisis*""")

        print(quoi_faire)

        decision = (input("Entrez votre decision:"))
        if decision == "1":
            augmentation()
            combat()
            statut_partie()
            print("Lancé du dé:" + str(score_dé_final))
            nouveau_niveau_vie()
            gange_perdu()
            print(minimum)
            print(maximum)
            print("Dernier combat = " + str(combat_statut) + "\nNiveau de vie = " + str(
                niveau_vie) + "\nNombre de victoires consécutives =" + str(nombres_de_victoires))
            print()

        elif decision == "2":
            contourner_monstre()
            print("Niveau de vie mise a jour:" + str(niveau_vie))

        elif decision == "3":
            instructions()

        elif decision == "4":
            print("Merci et aurevoir!")
            boucle_jeu = False

        elif niveau_vie <= 0:
            print("La partie est terminée, vous avez vaincu " + str(nombres_de_victoires) + " monstre(s)")
            boucle_jeu = False


while autre_partie == "o":
    global niveau_vie
    niveau_vie = 20
    jeu()
    autre_partie = input("Voulez voulez faire une autre partie (o/n)")