# class Voiture: création d'une class
#     marque = "Audi" création d'un attribut qui est une variable 
#     couleur = "blanc"

# # print(Voiture.marque) j'appelle l'atribut de la marque de ma voiture

# voiture_01 = Voiture() création d'une instance à partir de la class Voiture, pour appeller l'instance il faut mettre les () comme les fonctions
# voiture_02 = Voiture()
# print(voiture_01.marque) j'appelle l'instance de voiture01 qui vaut les valeur de la class Voiture
# print(voiture_02.marque)

# # Voiture.marque = "Porsche" change totalement la marque de la voiture d'origine

# # print(voiture_01.marque)

# voiture_01.marque = "Opel"
# voiture_02.marque = "Seat"

# print(Voiture.marque)
# print(voiture_01.marque)
# print(voiture_02.marque)

class VoitureDeLuxe:
    voiture_crees = 0
    def __init__(self, marque):
        VoitureDeLuxe.voiture_crees += 1
        self.marque = marque

voiture_01 = VoitureDeLuxe("Lamborghini")
voiture_02 = VoitureDeLuxe("Porsche")
print(voiture_01.marque)
print(voiture_02.marque)
print(VoitureDeLuxe.voiture_crees)