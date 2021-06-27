#Leonardo Altamirano Retto
#Software A1
#Superficie de un circulo para un radio cualquiera.

class AcumuladorTotalizador:
    def __init__(self):
        pass
    
    def ContAcu(self):
        Num=[7,2,3,7,9,8,4,6,8,2]
        Cont=0
        Acu=0
        for total in Num:
            Acu=Acu+total
            Cont=Cont+1
        print("El valor contado es: {} y el valor acumulado es: {}", format(Cont,Acu))
        
Total=AcumuladorTotalizador()
Total.ContAcu()
      