#Leonardo Altamirano Retto
#Software A1
#Elabore pseudocódigo para el caso en que se desean escribir los números del 1 al 100.

class Numeros:
    def __init__(self):
        pass
    
    def Digitar(self):
        Num=int(input("Ingrese el numero: "))
        i=1
        while i <=100:
            print(i)
            i = i + 1
            
Total=Numeros()
Total.Digitar() 