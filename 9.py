def cuadrado(altura, anchura):
    for x in range(1, anchura+1):
        if x == anchura or x == 1:
            print(anchura*"*")
        else:
            for i in range(1, altura):
                    print("*", (altura-4)*" ", "*")

anchura = 5
altura = 3

cuadrado(altura, anchura)