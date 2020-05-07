class Livre:
    def __init__(self, nom, nombre_de_pages, prix): # init pour inialiser nos instance avec différentes valeurs
        self.nom = nom # 3 attributs créer
        self.nombre_de_pages = nombre_de_pages
        self.prix = prix
    
livre_HP = Livre("Harry Potter", 300, 10.99) # création de deux instances à partir de notre class livre
livre_LOTR = Livre("Le Seigneur des Anneaux", 400, 13.99) 
print(livre_HP.nombre_de_pages) # on applique la méthode. sur l'instance
print(livre_LOTR.nom)