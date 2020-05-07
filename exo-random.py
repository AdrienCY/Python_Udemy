import random

a = random.randint(0, 100)
b = random.randint(0, 100)

if a < b:
    print(f"Le nombre{b} est plus grand que le nombre {a}")

elif a > b:
    print(f"Le nombre {a} est plus grand que le nombre {b}")

else:
    print(f"Le nombre {a} et le nombre {b} sont égaux ")