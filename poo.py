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
    def attaquer(self, cible):

        attaque = random.randint(1,20)
        print(attaque)
        if attaque == 20:
           nombre = random.randint(1,8)
        elif attaque ==1:
            nombre = random.randint(0)

        elif attaque in range(2, 19):
            if attaque >= self.classe_armure(cible):
                nombre = random.randint(1,6)
            else:
                nombre = random.randint(0)

        cible.subir_dommages(nombre)




objet=NPC()
objet.nom= "nom"
objet.afficher_caracteristiques()
player=Kobold()
player.attaquer('character')
player.subir_dommages()
winner = Hero()
winner.attaquer(Kobold)