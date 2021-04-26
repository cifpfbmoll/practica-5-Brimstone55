def imprimirTrianguloInvertido(altura):
    for i in range (altura,0,-1):
        print (i*"*")

def imprimirTriangulo(altura):
    for i in range (1,altura):
        print (i*"*")
    return "Ha ido bien"

altura = int(input("dame la altura"))
imprimirTriangulo(altura)
imprimirTrianguloInvertido(altura)