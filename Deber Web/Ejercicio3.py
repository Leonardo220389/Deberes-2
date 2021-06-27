#Leonardo Altamirano Retto
#Software A1
#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas.
#El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por 
# las tres ventas que realiza en el mes y el total que recibirá en el mes tomando 
# en cuenta su sueldo base y sus comisiones.
class Pago:
    def __init__(self):
        pass
    
    def valorPagar(self):
        Valor1=float(input("Ingrese la primera venta: "))
        Valor2=float(input("Ingrese la segunda venta: "))
        Valor3=float(input("Ingrese la tercera venta: "))
        Subtotal=Valor1+Valor2+Valor3
        SueldoBase=500
        Comision=Subtotal*0.10
        TotalRecibir=SueldoBase+Comision
        print("El total a pagar es: {}".format(TotalRecibir))
        
valorTotal=Pago()
valorTotal.valorPagar()       