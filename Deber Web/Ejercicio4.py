#Leonardo Altamirano Retto
#Software A1
#Construir un algoritmo tal, que dado como dato la calificación de un alumno en un examen.

class Calificacion:
    def __init__(self):
        pass
    
    def Nota(self):
        Cali=float(input("Ingrese la calificación: "))
        if Cali >= 7:
            print("Aprobado")

notafinal=Calificacion()
notafinal.Nota()        