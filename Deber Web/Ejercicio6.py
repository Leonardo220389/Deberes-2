#Leonardo Altamirano Retto
#Software A1
#Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene
#un aumento del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento.

class SueldoPagar:
    def __init__(self):
        pass
    
    def Pago(self):
        Sueldo=int(input("Ingrese el valor del sueldo: "))
        if Sueldo < 600:
            Aumento= Sueldo * 0.10
            NuevoSueldo= Sueldo + Aumento
        else:
            NuevoSueldo=Sueldo
        print("El sueldo a pagar es de: {}".format(NuevoSueldo))
        
SueldoTotal=SueldoPagar()
SueldoTotal.Pago()