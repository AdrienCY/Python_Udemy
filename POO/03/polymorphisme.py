class Vehicule:
    def avance(self):
        print("le véhicule démarre")

class Voiture(Vehicule):
    def avance(self):
        super().avance()
        print("la voiture roule")

class Avion(Vehicule):
    def avance(self):
        super().avance()
        print("l'avion vol")

v = Voiture()
a = Avion()
v.avance()
a.avance()