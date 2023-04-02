import arcade
import random

#variable pour la largeur et la hauteur de la fenetre (respectivement) sont egale a 800 pixels et 600 pixels
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800

#variable couleur est agale a une liste de couleurs de la librarie arcade
COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,arcade.color.GOLDEN_POPPY, arcade.color.TURQUOISE_BLUE,arcade.color.SPRING_GREEN,arcade.color.RED,arcade.color.LAVENDER_INDIGO]

#créer l'objet Balle:methodes pour definir les parametre de l'objet, permetre changer de position sur la fenetre (bouger en restant dans le cadre), et de dessiner l'objet balle d'après les parametres
class Balle():

#methode intit: les atributs propriétés du cercle (ex:le position actuel (x,y) balle, le position/vitessse par lequel il se deplace(x,y)) sont egale a des parametres
    def __init__(self, rayon,position_x,position_y, vitesse_deplacement_x, vitesse_deplacement_y, couleur):
        self.rayon = rayon
        self.centre_x = position_x
        self.centre_y = position_y
        self.change_x = vitesse_deplacement_x
        self.change_y = vitesse_deplacement_y
        self.color = couleur

#methode on_update definit deplacement balle(coordone actuel + la valeur par lequel ils se deplace) et permet balle de ne pas sortir du cadre en utilisant position x,y actuelle
    def on_update(self):
        self.centre_x += self.change_x
        self.centre_y += self.change_y
        # conditions pour veirifier la position de la bale (x,y) et de le faire "rebondir" sur bords cadre en rendant opposé et inverse la valeur de changement position(x,y)
        if self.centre_x < self.rayon:
            self.change_x *= -1

        if self.centre_x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1

        if self.centre_y < self.rayon:
            self.change_y *= -1

        if self.centre_y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1


#methode dessiner balle sur la fenetre d'après fonction et les atributs propriétés balle
    def draw(self):
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


#créer l'objet Rectangle:methodes pour definir les parametre de l'objet, permetre changer de position sur la fenetre (bouger en restant dans le cadre), et de dessiner l'objet rectangle d'après les parametres
class Rectangle():

# methode intit: les atributs propriétés du rectangle (ex:le position actuel (x,y) rectangle, le position/vitessse par lequel il se deplace(x,y)) sont egale a des parametres
    def __init__(self,position_x,position_y, vitesse_deplacement_x, vitesse_deplacement_y, largeur, hauteur, couleur, nombre_float):

        self.centre_x = position_x
        self.centre_y = position_y
        self.change_x = vitesse_deplacement_x
        self.change_y = vitesse_deplacement_y
        self.width = largeur
        self.height = hauteur
        self.color = couleur
        self.angle = nombre_float

#methode on_update definit deplacement rectangle(coordone actuel + la valeur par lequel ils se deplace) et permet rectagnle de ne pas sortir du cadre en utilisant position x,y actuelle
    def on_update(self):
        self.centre_x += self.change_x
        self.centre_y += self.change_y
        #conditions pour veirifier la position du rectangle (x,y) et de le faire "rebondir" sur bords cadre en rendant opposé et inverse la valeur de changement position(x,y)
        if self.centre_x < self.width:
            self.change_x *= -1

        if self.centre_x > SCREEN_WIDTH - self.width:
            self.change_x *= -1

        if self.centre_y < self.height:
            self.change_y *= -1

        if self.centre_y > SCREEN_HEIGHT - self.height:
            self.change_y *= -1


#methode dessiner balle sur la fenetre d'après fonction et les atributs propriétés balle
    def draw(self):
        arcade.draw_rectangle_filled(self.centre_x, self.centre_y, self.width, self.height, self.color,self.angle)

#definir l'objet en le
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "TP4")
        self.liste_balles= []
        self.liste_rectangles= []

    def on_draw(self):
        arcade.start_render()
        for balle in self.liste_balles:
            balle.draw()
        for rectangle in self.liste_rectangles:
            rectangle.draw()

    def on_update(self, delta_time: float):
        for balle in self.liste_balles:
            balle.on_update()
        for rectangle in self.liste_rectangles:
            rectangle.on_update()



#methode: pour permetre d'afficher une balle a l'ecran l'endroit du clic boutton gauche et d'afficher un rectangle a l'ecran a l'endroit du clic boutton droit
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):

        #condition if le button clique est le boutton gauche
        if button == arcade.MOUSE_BUTTON_LEFT:

#atrribut rayon,change_x et change_y sont egale a des nb hasard entre un minimum et maxium donnée et celle color est egale a couleur (valeur) hasard dans la liste de couleurs (definir valeurs)
            rayon = random.randint(15, 50)
            change_x = random.randint(1,10)
            change_y = random.randint(1,10)
            color = random.choice(COLORS)
#variable balle est egale a l'objet Balle qui a les valeurs atributs definit ci-haut
            balle = Balle(rayon, x, y, change_x, change_y, color)
#ajouter un objet balle a la liste de balles
            self.liste_balles.append(balle)

        # condition if le button clique est le boutton droit
        if button == arcade.MOUSE_BUTTON_RIGHT:
# atrribut change_x et change_y,width et height sont egale a des nb hasard entre un minimum et maxium donnée, atribut angle est egale a un nb float (90.00)et celle color est egale a couleur (valeur) hasard dans la liste de couleurs (definir valeurs)
            change_x = random.randint(1,10)
            change_y = random.randint(1,10)
            width = random.randint(50,80)
            height =random.randint(50,80)
            angle = 90.00
            color = random.choice(COLORS)
#variable rectangle est egale a l'objet Rectangle qui a les valeurs atributs definit ci-haut
            rectangle = Rectangle(x, y, change_x, change_y,width, height, color, angle)
#ajouter un objet rectangle a la liste de rectangle
            self.liste_rectangles.append(rectangle)




def main():
    MyGame()
    arcade.run()


main()