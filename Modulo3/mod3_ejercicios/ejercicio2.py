
while True:
    v = float(input("INGRESE VELOCIDAD: "))
    cinturon = int(input("Colocate Cinturon de Seguridad (1 SI) (2 NO) : "))

    var =  print("Esta en los limites permitidos") if (v>=0 and v<=60.00 and cinturon!=2)   else(print("PAGA TU MULTA",50) if (v<=60.00 and cinturon==2) else(print("MULTA_60-100km/h: ",100,"SOLES") if (v>=0 and v>60 and v<=100 and cinturon!=2) else(print("MULTA_60-100km/h + SIN CINTURON: ",150,"SOLES") if (v>60 and v<=100 and cinturon==2) else(print("MULTA_100-130km/h: ",150,"SOLES")  if (v>100 and v<=130 and cinturon!=2) else(print("MULTA_100-130km/h + SIN CINTURON: ",200,"SOLES")  if (v>100 and v<=130 and cinturon==2) else(print("MULTA_130km/h - a mas: ",220,"SOLES")  if (v>=130 and v<=600 and cinturon!=2) else(print("MULTA_130km/h - a mas + SIN CINTURON: : ",270,"SOLES")  if (v>130 and v<=600 and cinturon==2) else(print("CUIDA TU VIDA")) ) ) ) ) ) ) )

    bool= int(input("DESEAS SEGUIR INGRESANDO LAS VELOCIDAD?  (1 SI) (2 NO) :  "))
    if bool!=1:
        break
print(":"*15,"::GRACIAS::HASTA LUEGO:",":"*15)


