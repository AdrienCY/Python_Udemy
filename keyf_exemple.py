d = {
       0:   {"prenom": "paul", # ceci est un dictionnaire
            "profession": "ingé",
            "ville": "bordeaux"},

       1:   {"prenom": "julie", # ceci est un dictionnaire
            "profession": "archi",
            "ville": "paris"},

       2:   {"prenom": "pierre", # ceci est un dictionnaire
            "profession": "plombier",
            "ville": "marseille"}

    }



d[0]["prenom"] # pour récuperer la clé en question
dictionnaire.get("prenom", "la clé 'prenom' n'existe pas") #permet de savoir si l'élément existe ou pas dans la liste et permet de retourner un message
d["prenom"] = "julie" # donc maintenant la valeur prenom vaut julie
d["age"] = 30 # ajoute une clé age, mais attention si cette clé existe elle la remplace
del d["age"] #permet de supprimer la valeur age
if "age" in d:
    del d["age"] # permet de savoir si la valeur age existe bien dans la variable d
d.keys() # permet de boucler dans un dictionnaire
d.values()
for cle in dictionnaire:
    print(cle)
    print(dictionnaire[cle])

[("prenom", "paul"), ("profession", "ingé"),("ville", "paris")]
dictionnaire.items() #méthode la plus simple pour récup
for cle, valeur in dictionnaire.items():
    print(cle, valeur)