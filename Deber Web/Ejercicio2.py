#Leonardo Altamirano Retto
#Software A1
#Para obtener el descuento es necesario conocer la cantidad total de la compra,
#y sobre ésta aplicar el 15%. Posteriormente, este descuento deberá ser sustraído de la 
#cantidad total de la compra para así obtener la cantidad con descuento, que es la que el cliente pagará.

class Compra:
    def __init__(self):
        pass
    
    def Descuento(self):
        Total=int(input("Ingrese el total de la compra: "))
        Desc=Total*0.15
        CantPagar=Total-Desc
        print("El valor a pagar con el descuento es: {}".format(CantPagar))
        
PagoTotal=Compra()
PagoTotal.Descuento()