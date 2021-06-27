#Leonardo Altamirano Retto
#Software A1
#Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2. 
#El aspirante que obtenga calificaciones mayores que 80 en ambos exámenes es aceptado; en caso contrario es rechazado.

class Calificaciones:
    def __init__(self):
        pass
    
    def Notas(self):
        C1=int(input("Ingrese la primera nota: "))
        C2=int(input("Ingrese la segunda nota: "))
        if (C1>=80) and (C2>=80):
            print("Aceptado")
        else:
            print("Rechazado")
            
NotaFinal=Calificaciones()
NotaFinal.Notas()