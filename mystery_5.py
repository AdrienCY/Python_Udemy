import random

nombre_mystere = random.randint(0, 50)
boucle = 0

while boucle < 5: # boucle inferieur à 5 et ingremente +1 dans chaque condition
    nombre = input("Quel est le nombre mystere ? ") # rentre la valeur

    if not nombre.isdigit(): # controle si c'est bien un chiffre
        print("Veuillez rentrer un nombre !")
        continue

    nombre = int(nombre) # le convertir en nombre

    if nombre < nombre_mystere:
        print(f"Le nombre mystère est plus grand que {nombre} ")
        boucle += 1

    elif nombre > nombre_mystere:
        print(f"Le nombre mystère est plus petit que {nombre}")
        boucle += 1

    else:
        print("Bravo, vous avez trouvé le nombre mystère !")
        exit()       

if boucle == 5: # si égal à 5 alors vous avez perdu et affiche le resultat
    print(f"Perdu ! le nombre mystère à trouver était le {nombre_mystere}")
    exit()
