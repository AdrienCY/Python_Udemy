# liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
# for i in liste:
#     if i % 2 == 1:
#         continue
#     else:
#         print(i)

liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombre_positifs = [i for i in liste if i > 0]
print(nombre_positifs)

liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombre_positifs = [i * 2 for i in liste if i > 0]
print(nombre_positifs)