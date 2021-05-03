
def conversor(tipo, monto):
    if tipo==1:
        return round(float(monto)*505.00,2)
    elif tipo==2:
        return round(float(monto)/516.00,2) 

def calcularcolones():
    dolares = input('Ingrese el monto en dolares ')
    colones = str(conversor(1,float(dolares)))
    print("Tienes " + colones + " colones") 

def calculardolares():
    dolares = input('Ingrese el monto en colones ')
    colones = str(conversor(2,float(dolares)))
    print("Tienes " + colones + " dolares") 

print("1- Dolares a Colones")
print("2- Colones a Dolares")
opcion = input()
if opcion == "1":
    calcularcolones()
else:
    calculardolares()