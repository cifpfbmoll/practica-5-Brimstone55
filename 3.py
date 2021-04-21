num1 = int(input("Dame el primer número"))
num2 = int(input("Dame el segundo número"))
lista=[]
suma=0

if num1 <= num2:
    for numero in range(num1, num2+1):
        lista+=[numero]
        suma=suma+numero
    print("La suma desde", num1, "hasta", num2, "es:", suma)
else:
    print("ERROR: El primer número es menor o igual al segundo")