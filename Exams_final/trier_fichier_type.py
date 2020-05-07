import os
from glob import glob
import shutil
from pprint import pprint

chemin = r"A:\Python_Udemy\Exams_final\tri_fichiers_sources" # chemin qui correspond à mon fichier

extensions = {".mp3": "Musique",
             ".wav": "Musique",
             ".mp4": "Videos",
             ".mov": "Videos",
             ".jpeg": "Images",
             ".jpg": "Images",
             ".png": "Images",
             ".pdf": "Documents"}

fichier = glob(os.path.join(chemin, "*")) # on créer une variable qui permet de joindre notre chemin l'étoile sert à remplacer à la fin les deux etoile /**
pprint(fichier) # permet d'afficher tout les fichier qui sont présent dans la variable fichier qu'on à join auparavant
for fichier in fichier: # on boucle dans fichier qui va etre récuperé dans la variable fichier
    extension = os.path.splitext(fichier) [-1] #splitext permet de spliter sur le point. et de récuperer l'extension grâce à -1, extension sera égale à .mp3
    dossier = extensions.get(extension) #s'il trouve la valeur ".mp3" de la variable extension alors il va retourner "musique" - extensions corresponds au dictonnaire
    if dossier: #si dossier est vrai
        chemin_dossier = os.path.join(chemin, dossier) #join le chemin du dossier de base avec le dossier qu'on a récuperer par rapport à la valeur .mp3 donc rajout le dossier musique
        os.makedirs(chemin_dossier, exist_ok=True) # s'assure si le dossier existe ou pas, et va le créer
        shutil.move(fichier,chemin_dossier) #fichier c'est le chemin complet vers le fichier avec l'extension et qu'on veut le deplacer vers le chemin_dossier donc qui vaut
        #qui vaut au dossier créer par rapport à son extension