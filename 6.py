triangulo = int(input("altura"))

for x in range (1, triangulo + 1):
    for y in range(x):
        print("*", end="")
    print("")