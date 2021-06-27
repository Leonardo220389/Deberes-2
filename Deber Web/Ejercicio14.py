#Leonardo Altamirano Retto
#Software A1
#Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, 
#utilizando un bucle controlado por el usuario.

class SumPro:
    def __init__(self):
        pass
    
    def SumaProduc(self):
        Suma=0
        Produ=1
        Num=0
        Resp= input
        while (Resp != "N") and (Resp != "n"):
            Num=int(input("Ingrese un numero entero: "))
            Suma=Suma+Num
            Produ=Produ*Num
            Resp= input("Desea Continuar(S/N)?")
        print("La suma es: {} y el producto es: {}".format(Suma,Produ))

Total=SumPro()
Total.SumaProduc()