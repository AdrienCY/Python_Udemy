import json

chemin = "C:/Users/AdrienCy/Documents/fichier.json"

# with open(chemin, "r", encoding="utf-8") as f: # permet d'ouvir et de fermernotre fichier encoder en utf8
#     contenu = f.read().splitlines() # permet de lire notre fichier et chaque retour de ligne est enregistrer dans une liste
#     print(contenu)

# with open(chemin, "a") as f: # w ecrase la valeur du fichier, a permet d'ajouter
#      f.write("\nBonjour")

with open(chemin, "r") as f:
    # json.dump(list(range(10)), f, indent=4) # dump permet d'écrire dans un fichier j.son
    liste = json.load(f) # lire un fichier json et on utilise la fonction type pour connaitre le retour
    print(type(liste))

#erreur courante

chemin = "C:/Users/AdrienCy/Documents/info.txt"
f = open(chemin, "r") # la variable f ouvre le chemin qui contient le fichier et lis grace à "r"
print(f.read()) # il vient de lire une premiere fois le curseur est tout en bas il faut le remettre en haut
f.seek(0) #curseur remis à zero
contenu = f.read() # relis une deuxieme fois 
print(contenu)
f.close

#toujour mettre une valeur dans le fichier Json sinon erreur
# si dans Json.dump il  a un caractère comme è, é cela va provoquer un code bizarre pour résoudre cela taper:

with open(chemin, "r") as f:
    json.dump("pèche", f, ensure_ascii=False) # permet d'enlever ce code bizarre
