#Leonardo Altamirano Retto
#Software A1
#Determinar si un número entero proporcionado por el usuario es primo. 
#Un número primo es un entero que no tiene más divisores que él mismo y la unidad.
#Elaborar Pseudocódigo

class NumPrimo:
    def __init__(self):
        pass
    
    def Primo(self):
        div, num, res=0,0,0
        primo=True
        div=2
        num=int(input("Ingrese a un numero: "))
        while (div < num) and (primo == True):
            res=num%div
            if res==0:
                primo=False
            div=div+1
        if primo == True:
            print("Numero", num, "es primo")
        else:
            print("Numero", num, "no es primo") 

Total=NumPrimo()
Total.Primo()