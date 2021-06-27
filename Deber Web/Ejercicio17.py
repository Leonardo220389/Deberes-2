#Leonardo Altamirano Retto
#Software A1
#Aplicar los pasos de la metodología para la solución de un problema para leer un número entero N y calcular el resultado de la siguiente serie:
#1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N. Resolveremos el problema utilizando bucle Repeat controlado por contador y usando banderas.
class Series:
    def __init__(self):
        pass
    
    def Codigo(self):
        Serie=0
        I=1
        band=True
        Num=int(input("Ingrese un numero: "))
        while I <= Num:
            if band == True:
                Serie=Serie+(1/I)
                band=False
            else:
                Serie=Serie-(1/I)
                band=True
            I=I+1
        print("El valor es: ", Serie)

Total=Series()
Total.Codigo()
        