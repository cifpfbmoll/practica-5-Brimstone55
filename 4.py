num = int(input("Dame el número para calcular su factorial"))
fin = 0
lista = []
multiplica = num

for x in range(num-1):
    lista+=[x]
    multiplica = multiplica * x
    print(multiplica)
