#classe stringfoo qui contient informations pour accepter un string et le sauvgarder dans un attribut puis qui a la possilibité de l'imprimer
class StringFoo:
    #fonction qui contient informations sur la variable name qui pour l'instat est vide (objet créer)
    def __init__(self):
        self.name = " "
    #fonction qui permetre d'attribuer un valeur au variable nom (objet définit)
    def set_string(self, parametre):
            self.name = parametre
    #fonction qui permet d'impirimer la valeur du variable nom en lettre majuscule

    def print_string(self):
        print(self.name.upper())

foo=StringFoo()
foo.set_string('oui')
foo.print_string()


foo.set_string('ou')
foo.print_string()
