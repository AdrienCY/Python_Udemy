# # Demander à l'utilisateur d'entrer un premier nombre

# # Demander à l'utilisateur d'entrer un deuxième nombre

# # Afficher à l'écran le résultat de l'addition (exemple : 'Le résultat de l'addition de 5 avec 10 est égal à 15')

# a = int(input("entrer un premier nombre : "))
# b = int(input("entrer le deuxième nombre : "))

# result = f"Le resultat de l'addition de {a} avec {b} est égal à {a + b}"
# print(result)

# # Phrases à afficher :

# # J'ai une classe de 30 élèves

# # 10 + 5 est égal à 15

# # 15

# # L'addition de 10 + 5 est égal à 15

# nombre_a = int(30)
# a = f"J'ai une classe de {nombre_a} élèves"
# b_one = int(10)
# b_two = int(5)
# b = f"{b_one} + {b_two} est égal à {b_one + b_two}"
# c = 10 + int(5)
# d = f"L'addition de 10 + 5 est égal à {c}"

# Demander à l'utilisateur d'entrer un nombre pour tenter de deviner le nombre mystère.

# Afficher si le nombre entré par l'utilisateur est égal au nombre mystère (afficher un booléen True ou False).

# mystere = 7
# a = int(input("deviner le nombre mystère: "))

# result = a == mystere
# print(result)

# a = 10
# if age >= 18:
#     print("Vous êtes majeur")
# elif age < 18:
#     print("Vous êtes mineur")
# else:
#     print("Vous n'êtes ni majeur ni mineur")

user = "admin"
mdp = "admin"
if mdp == "admin" or user == "admin":
    print("Bienvenue !")