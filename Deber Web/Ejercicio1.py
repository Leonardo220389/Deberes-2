#Leonardo Altamirano Retto
#Software A1
#Superficie de un circulo para un radio cualquiera.

class SuperficieCirculo:
    def __init__(self):
        pass
    
    def Circulo(self):
        Sup = 0
        Pi = 3.1416
        Radio=int(input("Ingrese el radio: "))
        Sup = Pi * (pow(Radio, 2))
        print("La superficie del circulo es: {}".format(Sup))

Respuesta=SuperficieCirculo()
Respuesta.Circulo()
