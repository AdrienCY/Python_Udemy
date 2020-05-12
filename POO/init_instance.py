# class Voiture:
#     voiture_crees = 0
#     def __init__(self,  marque):
#         Voiture.voiture_crees += 1
#         self.marque = marque

# voiture_01 = Voiture("Lambo")
# voiture_02 = Voiture("Nissan")
# print(voiture_01.marque)
# print(voiture_02.marque)
# print(Voiture.voiture_crees)


class Voiture:
    def __init__(self): #Créez une classe voiture avec un attribut ‘essence’ qui est égal à 100.
        self.essence = 100

    def afficher_reservoir(self): # Créez une méthode ‘afficher_reservoir’ qui affiche le nombre de litres d’essence restant (‘La voiture contient x litres d’essence’).
        print(f"La voiture contient {self.essence} litres d’essence")

    def roule(self, km): #Créez une méthode ‘roule’ avec un paramètre km (kilomètre) qui va faire avancer la voiture et vider petit à petit le réservoir. 
        if self.essence <= 0: #Si le réservoir est vide quand on essaie de rouler, afficher la phrase :Vous n'avez plus d'essence, faites le plein ! et empêchez la voiture d’avancer
            print("Vous n'avez plus d'essence, faites le plein !")
            return

        self.essence -= (km*5) / 100 #On considère une consommation de 5L pour 100km, pour déterminer le nombre de litres d’essence nécessaire (km * 5) / 100

        if self.essence < 10: #Si la jauge d’essence descend en dessous de 10L, affichez la phrase : ‘Vous n'avez bientôt plus d'essence !’
            print("Vous n'avez bientôt plus d'essence !")

        self.afficher_reservoir()

    def faire_le_plein(self): #Créez une méthode ‘faire_le_plein’ qui remet le niveau d’essence à 100L et qui affiche la phrase 'Vous pouvez repartir !’
        self.essence = 100
        print("Vous pouvez repartir !")