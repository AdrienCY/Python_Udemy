projets = ["pr_GOT", "HP", "pr_Avengers"]

class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"Utilisateur {self.nom} {self.prenom}"   

    def affficher_projets(self):
        for projet in projets:
            print(projet)


class Junior(Utilisateur): # Junior hérite de Utilisateur et donc le code en dessous devient obsolete
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom) # on envoie nom et prenom à la méthode init de la classe parent utilisateur, super permet de récuperer la classe parent utilisateur

    def affficher_projets(self):
        for projet in projets:
            if not projet.startswith("pr_"):
                print(projet)

paul = Junior("Paul", "Durand")
print(paul)
paul.affficher_projets()