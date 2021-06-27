#Leonardo Altamirano Retto
#Software A1
#Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.

class MayorNum:
    def __init__(self):
        pass
    
    def Nums(self):
        Num1=int(input("Ingrese el primer numero: "))
        Num2=int(input("Ingrese el segundo numero: "))
        Num3=int(input("Ingrese el tercer numero: "))
        NM=0
        if (Num1 > Num2) and (Num1 > Num3):
            print("EL numero mayor es: ", Num1)
        elif (Num2 > Num3):
            print("EL numero mayor es: ", Num2)
        else:
            print("EL numero mayor es: ", Num3)
    
NumMayor=MayorNum()
NumMayor.Nums()