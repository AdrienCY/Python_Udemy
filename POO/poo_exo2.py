class Voiture: # la classe voiture
    pneus = 4 # l'attribut de classe

    def __init__(self, marque): # la méthode qui sera inialisé qui est égale à une fonction, la différence c'est une méthode appartient à une classe
        self.marque = marque # un attribut d'instance

lambo = Voiture("lamborghini") # instance qui définit à partir de la classe voiture