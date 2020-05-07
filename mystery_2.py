import random

nombre_mystere = random.randint(0, 10)
nombre = input("Devinez le chiffre mystere !: ")

if nombre.isdigit() == True:

    nombre = int(nombre)

    if nombre < nombre_mystere:
        print(f"Le nombre mystère est plus grand que {nombre} ")

    elif nombre > nombre_mystere:
        print(f"Le nombre mystère est plus petit que {nombre}")

    else:
        print("Bravo !")
else:
    print("Veuillez rentrer un nombre !")
