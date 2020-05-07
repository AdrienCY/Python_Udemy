import json

fichier = r"A:\Python_Udemy\BDD\settings.json"

with open(fichier, "r") as f:
    settings = json.load(f)
print(settings)

settings["fontSize"] = 15

with open(fichier, "w") as f:
    json.dump(settings, f, indent=4)

print()