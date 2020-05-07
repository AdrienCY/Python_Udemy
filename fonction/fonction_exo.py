import os
def retourne_cinq():
    return 5

a = retourne_cinq() #retourne 5
print (a)

def verif_fichier():
    if os.path.exists("fichier.txt"): # soit le fichier existe il retourne true soit c'est pas le cas et il return false
        return True
    return False

b = verif_fichier()
print (b)

def addition (a, b):
    return a + b

c = addition(10, 5)
print(c)

a = 5
def add(a=1, b=2):
    return a + b
    
d = add(a)
print(d)

def foo():
    a = 5
    print(a)
    
a = 10
foo()
print(a)

e = 5
m = 10

def plus():
    global e
    e+= 8
    print(e)
plus()