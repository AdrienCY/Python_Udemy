fichier = input("entrez un fichier à ouvrir :")
fichier1 = fichier + r""

try:
    f = open(fichier1, "r")
    print(f.read())
except FileNotFoundError:
    print("le fichier est introuvable")
except UnicodeDecodeError:
    print("impossible d'ouvrir le fichier")
else:
    f.close()