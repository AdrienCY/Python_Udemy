a = 10
b = 2
# print(a / b) # retourne une erreur zerodivision

try:
    resultat = (a / b)
except ZeroDivisionError:
    print("Division par zero impossible")
except TypeError:
    print("la variable n'est pas du bon type")
except NameError as e:
    print("Erreur :", e)
else:
    print(resultat)

# finally: #permet de valider quelque soit le resultat
