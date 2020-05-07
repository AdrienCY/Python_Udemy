import sqlite3

conn = sqlite3.connect("database.db") # onnexion à la bdd
c = conn.cursor() # on créer un curseur qui permet d'éxecuter des requete sql

c.execute("""
CREATE TABLE IF NOT EXISTS employees(
    prenom text,
    nom text,
    salaire int
)
""") # le curseur est pointé vers une requete en sql

c.execute("DELETE FROM employees WHERE prenom = 'Paul'")
# d = {"salaire": 15000, "prenom": "Paul", "nom": "Dupond"} # on associe à la clé a paul, le dictonnaire vaut d
# c.execute("INSERT INTO employees VALUES (:prenom, :nom, :salaire)", d) # on insert comme valeur dans a et b qui sont dans d de dicto qui passe par la méthode execute

# c.execute("SELECT * FROM employees WHERE prenom=:prenom", d) # permet de récuperer dans une table certains éléments

# c.execute(""" UPDATE employees SET salaire=:salaire 
# WHERE prenom=:prenom AND nom=:nom""", d) # permet de mettre à jour la bdd et de séléctionner un nom appartenant à se nom et de changer la valeur comme le salaire

# c.execute("SELECT * FROM employees")
# donnees = c.fetchall() # permet de récuperer toute les données de la requete sql select * from. fetchall est un générateur, une fois utilisé il est épuisé
# print(donnees)

# premier = c.fetchone() # permet de séléctionner qu'un utilisateur dans la bdd, si le fetchall à été épuisé alors la méthode fetchone sera épuisé et affichera none
# print(premier)
# deuxieme = c.fetchone()
# print(deuxieme)

conn.commit()# permet d'envoyer la requete dans la bdd
conn.close() # fermeture bdd