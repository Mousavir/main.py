# Exercice POO2
# Rozhina Mousavi
# Janvier 2023

import random

def calcul():
    global list_nombre

    list_nombre = random.sample(range(1, 6), 4)

    list_nombre.sort()
    return (list_nombre[3] + list_nombre[2] + list_nombre[1])


class NPC:
    def __init__(self):
        self.force = calcul()
        self.agilite =calcul()
        self.constitution =calcul()
        self.intelligence =calcul()
        self.sagesse = calcul()
        self.charisme = calcul()
        self.classe_armure = random.randint(1,12)
        self.nom = " "
        self.race = " "
        self.espece = " "
        self.point_de_vie = random.randint(1,20)
        self.profession = " "

    def afficher_caracteristiques(self):
        print("Caractéristiques du personnage: Force:", self.force, "Agilité:", self.agilite," Constitution:",self.constitution," Intelligence:", self.intelligence, "Sagesse:",self.sagesse, "Charisme:",self.charisme, " Classe d'armure:",self.classe_armure," Nom:",self.nom," Race:",self.race, " Espèce:",self.espece, " Point de vie:",self.point_de_vie," Profession:",self.profession)

class Kobold(NPC):
    def attaquer(self,parametre_1):
        return

    def subir_dommages(self,parametre_2):
        self.point_de_vie -= parametre_2


class Hero(NPC):
    def attaquer(self, cible = Kobold):
        global attaque
        attaque = random.randint(1,20)
        cible.subir_dommages(5)

    dommages_attaque_critique = random.randint(1, 8)
    dommages_attaque = random.randint(1, 6)
    if attaque == 20:
        self.force - dommages_attaque_critique

    elif attaque == 1:
        return

    elif attaque in range(2, 19):
        if attaque >= self.classe_armure:
            self.force - dommages_attaque
        else:
            return

    def subir_dommages(self):



objet=NPC()
objet.nom= "nom"
objet.afficher_caracteristiques()
player=Kobold()
player.attaquer('character')
player.subir_dommages(6)
winner = Hero()
winner.attaquer()
winner.subir_dommages()