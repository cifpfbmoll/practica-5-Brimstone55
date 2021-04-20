numero1 = int(input("dame el número más alto"))
numero2 = int(input("dame el número más bajo"))

if numero1 < numero2:
    print("ERROR: El segundo número es más alto")
else:
    numero1 = numero1 + 1
    for x in range(numero2, numero1):
        if x % 2 == 1:
            print(x, "es impar")
        else:
            print(x, "es par")