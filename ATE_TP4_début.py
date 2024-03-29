import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,arcade.color.GOLDEN_POPPY, arcade.color.TURQUOISE_BLUE,arcade.color.SPRING_GREEN,arcade.color.RED,arcade.color.LAVENDER_INDIGO]

class Rectangle():
    def __init__(self,position_x,position_y, vitesse_deplacement_x, vitesse_deplacement_y, largeur, hauteur, couleur, nombre_float):

        self.centre_x = position_x
        self.centre_y = position_y
        self.change_x = vitesse_deplacement_x
        self.change_y = vitesse_deplacement_y
        self.width = largeur
        self.height = hauteur
        self.color = couleur
        self.angle = nombre_float

    def on_update(self):
        self.centre_x += self.change_x
        self.centre_y += self.change_y

        if self.centre_x < self.width:
            self.change_x *= -1

        if self.centre_x > SCREEN_WIDTH - self.width:
            self.change_x *= -1

        if self.centre_y < self.height:
            self.change_y *= -1

        if self.centre_y > SCREEN_HEIGHT - self.height:
            self.change_y *= -1



    def draw(self):
        arcade.draw_rectangle_filled(self.centre_x, self.centre_y, self.width, self.height, self.color,self.angle)



class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_rectangles= []
    def on_draw(self):
        arcade.start_render()
        for rectangle in self.liste_rectangles:
            rectangle.draw()
    def on_update(self, delta_time: float):
        for rectangle in self.liste_rectangles:
            rectangle.on_update()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):

        if button == arcade.MOUSE_BUTTON_RIGHT:

            change_x = random.randint(1,10)
            change_y = random.randint(1,10)
            width = 20
            height =40
            angle = 90.00
            color = arcade.color.BLUE
            rectangle = Rectangle(x, y, change_x, change_y,width, height, color, angle)
            self.liste_rectangles.append(rectangle)




def main():
    MyGame()
    arcade.run()


main()