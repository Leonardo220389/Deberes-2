#Leonardo Altamirano Retto
#Software A1
#Diseñe un pseudocódigo para calcular la suma y producto 
#de N números enteros, utilizando un bucle controlado por centinela.
class SumPro:
    def __init__(self):
        pass
    
    def SumaProduc(self):
        Suma=0
        Produ=1
        Num=int(input("Ingrese un numero entero: "))
        while (Num != -1):
            Suma=Suma+Num
            Produ=Produ*Num
            Num=int(input("Ingrese un numero entero: "))
        print("La suma es: {} y el producto es: {}".format(Suma,Produ))

Total=SumPro()
Total.SumaProduc()