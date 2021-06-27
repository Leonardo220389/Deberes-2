#Leonardo Altamirano Retto
#Software A1
#Aplicar las fases  para  la resolución de un problema para leer un vector de 20 números enteros
#y a continuación escribir en un vector A todos los números negativos y en un vector B todos los 
#positivos o iguales a cero. Imprimir dichos vectores.

from Deber.Ejercicio11 import Total


class Vector:
    def __init__(self):
        pass
    
    def Calculo(self):
        j=1
        k=1
        for i in 20:
            Num=int(input("Ingrese el valor: "))
            if Num > 0:
                j=j+1
            else:
                k=k+1
        for i in j:
            print(i)
        for i in k:
            print(i)
            
Total=Vector()
Total.Calculo()
