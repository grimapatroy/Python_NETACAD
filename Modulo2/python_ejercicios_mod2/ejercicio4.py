
pan = 2.0
torta = 5.0
cafe = 3.5

# descuento monto total
# si no s evende ni un producto es le coloca cero

print("BIENVENIDOS AL SISTEMA DE VENTAS \n")
canPan = int(input("INGRESE ELNUMERO DE UNIDADES DE PAN VENDIDAS: "))
canTorta = int(input("INGRESE ELNUMERO DE UNIDADES DE TORAS VENDIDAS: "))
canCafe = int(input("INGRESE ELNUMERO DE UNIDADES DE CAFES VENDIDAS: "))
print("*"*100)
total = float((canPan*pan) + (canCafe*cafe) + (canTorta*torta))
print("PRECIO TOTAL SIN DESCUENTO: "+ str(total) + " SOLES")

print("NOTA: El descuento puede ser entre 1% y 50%")
descuento = float(input("INGRESE EL DESCUENTO: "))
print("*"*100)
print("EL TOTAL DEL DESCUENTO ES: "+ str( round(total*(descuento/100),2) ) + " SOLES")
print("MONTO FINAL DE VENTA: " + str( round(total - (total*(descuento/100) ),2 ) ) + " SOLES")
print("*"*100)
