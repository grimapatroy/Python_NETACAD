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

# utilize lista para las tarifas y otro para los bonos
    listaTarifa = [.50 , 1.00 , 1.50]
    listaPrenda = ["POLO","CAMISA","PANTALON"]
    listaBonos = [250.00, 150.00 ,100.00 , 50.00]
    listaCategoria = ["A","B","C","D"]
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

    for i in range(0,len(listaTarifa)+1):
        if listaPrenda[i]==tipoPrenda:
            pagoTarifa = listaTarifa[i]
            break

    for i in range(0,len(listaCategoria)+1):
        if cantPrendas > 700 and listaCategoria[i] == categoriaBoni:
            pagoBoni = listaBonos[i]
            break
        else:
            pagoBoni = 0.0

    SueldoBruto = (pagoTarifa*cantPrendas) + pagoBoni
    print("/"*20,"SU SUELDO NETO ES: " +  str(round((SueldoBruto - SueldoBruto*.09 - SueldoBruto*.02),2)), "DESCUENTO POR IMPUESTOS: " + str(round(SueldoBruto*.09)),"DESCUENTO POR SEGURO: "+ str(round(SueldoBruto*.02)),"/"*20,sep="\n")
    bool= int(input("DESEAS SEGUIR CALCULANDO SUELDOS?  (1 SI) (2 NO) :  "))
    if bool!=1:
        break
    print("-"*120)
print(":"*15,"::GRACIAS::HASTA LUEGO:",":"*15)
