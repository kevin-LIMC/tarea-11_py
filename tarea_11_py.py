
def NTablas():
    T = 1
    NUM = int(input("\nCuantas Tablas: "))

    while(T <= NUM ):
        I =10
        while(I  >= 1):
            print(f"{T} x {I} = {T*I}")
            I -= 1
        input("Pulse enter para continuar")
        T += 1


def TablasdeN():
    I = 1

    NUM = int(input("\nDigite un numero: "))

    while(I <= 12):
        print(f"{NUM} x {I} = {NUM*I}")
        I += 1

    input("Pulse enter para continuar")
#----------------------------------------------------

while True:
    Opcion = int(input("""\nSeleccione la funcion de su interes:\n
    1. Generador de Tablas de Multiplicar
    2. Tabla de Multiplicar de tu interes
    3. Salir\n 
    Opcion:"""))

    if  Opcion == 1:
        NTablas()
        

    elif Opcion == 2:
        TablasdeN()

    elif Opcion == 3:
        break
    else:
        print("Opcion invalida")



    
