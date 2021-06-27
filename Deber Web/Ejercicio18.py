#Leonardo Altamirano Retto
#Software A1
#Calcular el factorial de N números enteros leídos de teclado.

class Factorial:
    def __init__(self):
        pass
    
    def factorial(self):
        Numero=int(input("Ingrese el valor: "))
        acu=1
        for num in range(Numero, 1, -1):
            acu=acu*num
        print("Numero={}, factorial= {}".format(Numero,acu))

Total=Factorial()
Total.factorial()