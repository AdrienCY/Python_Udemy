employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }

if "id03" in employes:
    del employes["id03"] # permet de savoir si la valeur id003 existe bien dans la variable employes et supprime patrick
    print(employes)

employes["id02"]["age"] = 26 # ajoute une clé age, mais attention si cette clé existe elle la remplace
print(employes)

if "id01" in employes:
    age_paul = employes["id01"]["age"]
    print(age_paul)
