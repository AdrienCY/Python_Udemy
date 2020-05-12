class Voiture:
    voiture_crees = 0
    def __init__(self, marque, vitesse, prix):
        Voiture.voiture_crees += 1
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    @classmethod
    def lamborghini(cls): # cls represente la marque Voiture
        return cls(marque="Lamborghini", vitesse=250, prix=200000)

    @classmethod #méthode de classe
    def porsche(cls):
        return cls(marque="Porsche", vitesse=235, prix= 175000)

    @staticmethod # statique méthode, plus besoin de faire passer en parametre une classe
    def afficher_nombre_voitures():
        print(f"Vous avez {Voiture.voiture_crees} voitures dans votre garage.")

    def __str__(self): # méthode str
        return f"Voiture de marque {self.marque} avec vitesse maximale de {self.vitesse} et qui coûte {self.prix}."

lambo = Voiture.lamborghini() # la méthode de classe qui retourne une instance( return cls)
porsche = Voiture.porsche()
Voiture.afficher_nombre_voitures()
print(porsche)
affichage = str(porsche)
print(affichage)