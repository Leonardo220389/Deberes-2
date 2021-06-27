#Leonardo Altamirano Retto
#Software A1
#Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.


class Sumacuadrados:
    def __init__(self):
        pass
    
    def SumaNum(self):
        n=100
        Suma=0
        for i in range(1,n+1):
            Suma=Suma+i*i
        print("Total es: ",Suma)        
        
Total=Sumacuadrados()
Total.SumaNum()