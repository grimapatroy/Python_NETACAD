def val_prenda(prenda):
# funcion para verificar Prenda
    prenda=prenda.upper()
    val = True if prenda== "POLO" or prenda== "CAMISA" or prenda=="PANTALON" else False
    return val  if val else print("*"*50,"INGRESE LETRAS SOLO ESTAS  OPCIONES (POLO = PO) (CAMISA =C)(PANTALON =PA)","*"*50,end="\n")
def val_categoria(boni):
# funcion par aingreso corrcto de categoria
    boni=boni.upper()
    val = True if boni == "A" or boni =="B" or boni =="C" or boni=="D" else False
    return val  if val else print("*"*50,"INGRESE LETRAS SOLO ESTAS  OPCIONES (POLO) (CAMISA)(PANTALON)","*"*50,end="\n")
def val_datoNumerico(valor):
    val = True if  valor>0   else False
    return val if val else print("*"*50,"INGRESE SOLO NUMEROS ENTEROS Y MAYORES A CERO PARA LA CANTIDAD DE PRENDAS ","*"*50,end="\n")
pagoTarifa,pagoBoni,SueldoBruto= 0.0 , 0.0 , 0.0

while True:

    diccPrenda_Tarifa = {'POLO':.50,'CAMISA':1.50,'PANTALON':1.50}
    diccCatego_Bonus = {'A':250.00,'B':150.00,'C':100.00,'D':50.00}
    tipoPrenda = input("INGRESE EL TIPO DE PRENDA (POLO ) (CAMISA )(PANTALON ): ")
    cantPrendas = int(input("INGRESE LA CANTIDAD DE PRENDAS ELABORADAS: "))
    categoriaBoni = input("INGRESE CATEGORIA DEL OBRERO (A) (B)(C) (D): ")
    tipoPrenda=tipoPrenda.upper()
    categoriaBoni=categoriaBoni.upper()
    while not val_prenda(tipoPrenda):
        tipoPrenda = input("SE ACEPTAN SOLO LETRAS, VUELA A INGRESAR EL TIPO DE PRENDA (POLO ) (CAMISA)(PANTALON): ")
    while not val_categoria(categoriaBoni):
        categoriaBoni  = input("SE ACEPTAN SOLO LETRAS, VUELAVA A INGRESAR LA CATEGORIA DEL OBRERO (A) (B)(C) (D): ")
    while not val_datoNumerico(cantPrendas):
        cantPrendas = int(input("SE ACEPTAN SOLO NUMERO ENTEROS, VUELVA A INGRESAR LA CANTIDAD DE PRENDAS ELABORADAS : "))
    for key in diccPrenda_Tarifa:
        if tipoPrenda == key:
            pagoTarifa=diccPrenda_Tarifa[key]
            break
    for key in diccCatego_Bonus:
        if cantPrendas > 700 and key==categoriaBoni:
            pagoBoni = diccCatego_Bonus[key]
            break
        else:
            pagoBoni=0.0
    SueldoBruto = (pagoTarifa*cantPrendas) + pagoBoni
    print("/"*20,"SU SUELDO NETO ES: " +  str(round((SueldoBruto - SueldoBruto*.09 - SueldoBruto*.02),2)), "DESCUENTO POR IMPUESTOS: " + str(round(SueldoBruto*.09)),"DESCUENTO POR SEGURO: "+ str(round(SueldoBruto*.02)),"/"*20,sep="\n")
    bool= int(input("DESEAS SEGUIR CALCULANDO SUELDOS?  (1 SI) (2 NO) :  "))
    if bool!=1:
        break
    print("-"*120)
print(":"*15,"::GRACIAS::HASTA LUEGO:",":"*15)