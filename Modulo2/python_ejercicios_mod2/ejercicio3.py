panAnterior = float(input("INGRESE EL NUMERO DE BARRAS DE PAN VENDIDAS EL DIA ANTERIOR: "))
panHoy = float(input("INGRESE EL NUMERO DE BARRAS DE PAN VENDIDAS EL DIA DE HOY: "))

print("*"*150,"MONTO TOTAL DE BARRAS VENDIDAS DEL DIA: " + str(round((panHoy*10.55),2)) + " SOLES" , "DESCUENTO TOTAL POR BARRAS DEL DIA ANTERIOR: " + str(round( (((10.55*0.45))*panAnterior) ,2 ) ) + " SOLES", "MONTO TOTAL VENDIDO DE BARRAS DEL DIA ANTERIOR: "+   str(round( (panAnterior* (10.55 - (10.55*0.45)) ),2)) + " SOLES" , sep="\n")



# monto total a precio habitual
# descuento Total por ser  barras de ayer
# monto final de barras del dia anterior

print()