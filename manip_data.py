# Récupérez le premier et le dernier nombre contenus dans cette liste dans les variables 'nombre_premier' et 'nombre_dernier'.
nombres = [1, 2, 3, 4, 5, 4, 3, 2, 1]
nombre_premier = nombres[0]
nombre_dernier = nombres[-1]
 
# Récupérer l'élément 'Python' contenu dans la liste dans la variable 'langage'.
langages = ["Java", "Python", "C++"]
langage = langages[1]
 
# Changez la position de l'élément 'Python' dans la liste pour qu'il se retrouve à la fin de la liste (["Java", "C++", "Python"])
liste = ["Java", "Python", "C++"]
liste.remove("Python")
liste.append("Python")