import glob
import json

dossier = r"A:\Python_Udemy\dossier_exemple\**"
files = glob.glob(dossier, recursive=True)
chemin1 = r"A:\Python_Udemy\dossier_exemple\administratif\comptes_bancaires.json"
chemin2 = r"A:\Python_Udemy\dossier_exemple\administratif\securite_sociale.txt"

with open(chemin1, "r") as f:
    liste = json.load(f)
    # print(type(liste)) pour connaitre son type
    print(liste["Credit Mutuel"]["Numero de compte"])


with open(chemin2, "r") as fe:
    for line in fe:
        result = line.split(":")
        new = (result[-1])
        newtwo = "".join(new)
        print(newtwo)

#SOLUTION

import json
import glob

dossier = "/Users/thibh/formation-developpeur-python/dossier_exemple/**"
files = glob.glob(dossier, recursive=True)

numero_de_compte = None
numero_securite_sociale = None

for f in files:
    if f.endswith(".json"):
        with open(f, "r") as f:
            contenu = json.load(f)
            if "Credit Mutuel" in contenu:
                numero_de_compte = contenu["Credit Mutuel"]["Numero de compte"]
    elif f.endswith(".txt"):
        with open(f, "r") as f:
            contenu = f.read()
            if "Numéro de sécurité sociale" in contenu:
                numero_securite_sociale = contenu.split(":")[-1]

print(numero_de_compte)          
print(numero_securite_sociale)