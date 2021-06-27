#Leonardo Altamirano Retto
#Software A1
#Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, obtenga el resultado de la siguiente función.
print("""
Menu      
1=100*V
2=100^V
3=100/V
4=0
""")

class Numero:
    def __init__(self):
        pass
    
    def Escoja(self):
        Valor=int(input("Ingrese el valor: "))
        Total=0
        if Valor is 1:
            Total=100*Valor
        elif Valor is 2:
            Total=pow(100, Valor)
        elif Valor is 3:
            Total= 100/Valor
        else:
            Total=0
        print("La respuesta es: {}".format(Total))
        
Resultado=Numero()
Resultado.Escoja()


            