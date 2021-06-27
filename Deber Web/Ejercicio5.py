#Leonardo Altamirano Retto
#Software A1
#Dado como dato la calificación de un alumno en un examen, 
# escriba “aprobado” si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.
class Calificacion:
    def __init__(self):
        pass
    
    def Nota(self):
        Cali=float(input("Ingrese la calificación: "))
        if Cali >= 7:
            print("Aprobado")
        else:
            print("Reprobado")

notafinal=Calificacion()
notafinal.Nota()        