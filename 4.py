num = int(input("Dame el número para calcular su factorial"))
factorial = 1

for i in range(1, num + 1):
    print(i, factorial)
    factorial = factorial * i
print("El factorial de", num, "es:", factorial)