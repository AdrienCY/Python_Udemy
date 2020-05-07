from pprint import pprint

chemin = r"A:\Python_Udemy\Exams_final\prenoms.txt"
with open(chemin, "r") as f: # trouve le chemin et le mets en mode lecture dans la variable f
    lines = f.read().splitlines() #on lis et ont sépare les lignes de notre fichier ça enleve les retours à la ligne
    print(lines)

pprint(lines) # pour vérifier tout ça

prenoms = [] # créations d'une liste vide qui va récuperer chaque prenoms
for line in lines: # une boucle qui passe à l'interieur de chaque ligne de lines
    prenoms.extend(line.split()) # permet de rajouter plusieur élément d'un coup dans la liste, line.split() va nous retourner des prenoms

prenoms_final = [prenom.strip(",. ") for prenom in prenoms] #on boucle sur chaque prenom dans prenoms et on strip sur chaque prenom dans la liste
pprint(prenoms_final) # pour bien détailler chaque sorti de prenom

with open(chemin, "w") as f: # en mode écriture
    f.write("\n".join(sorted(prenoms_final))) #écrire chaque prenom dans mon fichier et trié avec retour à la ligne
