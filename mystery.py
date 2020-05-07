# Demander à l'utilisateur d'entrer un nombre pour tenter de deviner le nombre mystère.

# Afficher si le nombre entré par l'utilisateur est égal au nombre mystère (afficher un booléen True ou False).

# Afficher si le nombre entré par l'utilisateur est plus grand, plus petit ou égal au nombre mystère.

# nombre_mystere = 7
# nombre_utilisateur = int(input("Devinez le chiffre mystere !: "))

# if nombre_utilisateur < nombre_mystere:
#     print(f"Le nombre mystère est plus grand que {nombre_utilisateur} ")

# elif nombre_utilisateur > nombre_mystere:
#     print(f"Le nombre mystère est plus petit que {nombre_utilisateur}")

# elif nombre_utilisateur == nombre_mystere:
#     print("Bravo!")

import random

nombre_mystere = random.randint(0, 100)
nombre_utilisateur = int(input("Devinez le chiffre mystere !: "))

if nombre_utilisateur < nombre_mystere:
    print(f"Le nombre mystère est plus grand que {nombre_utilisateur} ")

elif nombre_utilisateur > nombre_mystere:
    print(f"Le nombre mystère est plus petit que {nombre_utilisateur}")

elif nombre_utilisateur == nombre_mystere:
    print("Bravo!")






