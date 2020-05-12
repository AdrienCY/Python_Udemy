import logging # permet de faire des niveaux de debug
import json # permet de sauvegarder notre liste dans un contenu json
import os # concatener et des operation sur notre disque dur avec les chemins de dossier

from les_constances import DATA_DIR # on importe notre module à nous du fichier les_constances

LOGGER = logging.getLogger() # niveau de debug

class Liste(list): # héritage des fonctions list dans ma Liste
    def __init__(self, nom): #référer à mon instances et le deuxieme parametre nom, self vaut Liste
        self.nom = nom # l'attribut .nom

    def ajouter(self, element): # méthode ajouter 
        if not isinstance(element, str): # je vérifie si element est de type str, si l'élément n'est pas de type string-> # alors on va lever une erreur de type
            raise ValueError("Vous ne pouvez ajouter que des chaînes de caractères!") 

        if element in self: # verifie si l'élément est dans l'instance, self c'est une list puisqu'on hérite de list
            LOGGER.error(f"{element} est déjà dans la liste.")
            return False
        
        self.append(element)
        return True # retourner un booleen pour etre sur que le code a était appliqué

    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        return False
    
    def afficher(self):
        print(f"Ma liste de {self.nom} :")
        for element in self:
            print(f" - {element}")

    def sauvegarder(self):
        chemin = os.path.join(DATA_DIR, f"{self.nom}.json") # joindre les differents chemins ensemble on joint notre constance data_dir avec le nom de ma liste
        if not os.path.exists(DATA_DIR): # on vérifie si le dossier existe
            os.makedirs(DATA_DIR) # on le créer

        with open(chemin, "w") as f: # on ouvre le dossier grâce au chemin complet en mode écriture qu'on recupere dans une variable f
            json.dump(self, f, indent=4) # on utilise notre module json pour écrire tout notre contenu dans ce fichier, self correspond à la liste, on écrit dans le fichier f

        return True

if __name__ == "__main__": # permet d'écrire du code dans cette structure conditionnellle
    liste = Liste("courses")
    # liste.ajouter(0)
    liste.ajouter("pommes")
    liste.ajouter("poires")
    # liste.ajouter("pommes")
    # liste.enlever("pommes")
    liste.sauvegarder()
