def validar_DatosNum(v1,v2):
    # val_esLetra ---> error si es letra
    # net =  True if (type(v1)==int and (type(v2)==float or type(v2)==int)) else False
    # val_esVacio --> error si es vacio o cadena
    val = True if  (v1>0 and v2>0 )  else False
    return val if val else print("*"*50,"INGRESE SOLO NUMEROS Y MAYORES A CERO PARA LA CANTIDAD DE VIAJES Y DISTANCIA ","*"*50,end="\n")
def validar_TipoCarga(tipo):
    val = True if (tipo=="F" and not tipo.isspace()) or (tipo=="NF"and not tipo.isspace()) else False
    return val if val else print("*"*50,"INGRESE LETRAS SOLO ESTA DOS OPCIONES (F=Fragil) y (NF=NO FRAGIL)","*"*50,end="\n")
while True:
    numViajes = int(input("Ingrese numero de Viajes: "))
    tipoCarga = input("Ingrese tipo de Carga (F=Fragil) y (NF=NO FRAGIL) : ")
    distancia =int(input("Ingrese la distancia recorrida en Kilometros del Punto de Partida y LLegada: "))
    while not validar_DatosNum(numViajes,distancia):
        numViajes = int(input("Vuelva a ingresar numero de Viajes: "))
        distancia =int(input("Vuelva a ingrese la distancia recorrida en Kilometros: "))
    while not validar_TipoCarga(tipoCarga):
        tipoCarga = input("Vuelva a ingrese tipo de Carga: ")
    costoDistancia = distancia*5 if  distancia>=5 else 25
    costoServicio = costoDistancia+(costoDistancia*0.2)  if  tipoCarga=="F"  else costoDistancia
    print("El Costo Total de Servicio es: "+str(costoServicio*numViajes)+" soles") if costoServicio*numViajes > 40 else (print("El Costo Total de Servicio es: 41 Soles "))
    print("-"*120)
    bool= int(input("DESEAS SEGUIR INGRESANDO MAS SERVICIOS?  (1 SI) (2 NO) :  "))
    if bool!=1:
        break
    print("-"*120)
print(":"*15,"::GRACIAS::HASTA LUEGO:",":"*15)


