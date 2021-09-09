while True:
    puntajeOb = float(input("INGRESE PUNTUACION OBTENIDA: "))
    resul =  "ERROR" if  puntajeOb<0   else (  "Inaceptable" if puntajeOb==0.0 else ("Aceptable" if puntajeOb==0.4 else ("Meritorio" if puntajeOb>=0.6 else "MAL"))     )

    monto = print(0.0*2400,resul) if resul=="Inaceptable" else( print(0.4*2400,resul) if resul =="Aceptable" else ( print(0.6*2400,resul)  if resul == "Meritorio" else ( print("PUNTACION INVALIDA !porfavor! INGRESE PUNTUACIONES EXACTAS como 0.0 0.4 0.6 a mas") if resul=="ERROR" else print("PUNTACION INVALIDA !porfavor! INGRESE PUNTUACIONES EXACTAS como 0.0 0.4 0.6 a mas")   )  ) )

    bool= int(input("DESEAS SEGUIR INGRESANDO MAS PUNTUACIONES?  (1 SI) (2 NO) :  "))
    if bool!=1:
        break
print(":"*15,"::GRACIAS::HASTA LUEGO:",":"*15)
