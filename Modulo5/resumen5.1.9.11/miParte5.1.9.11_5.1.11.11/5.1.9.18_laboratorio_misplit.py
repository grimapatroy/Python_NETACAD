def misplit(cadenita):
    inicio=0
    subCa = ""
    lista =[]
    pos=0
    if cadenita.isspace() or len(cadenita)==0:
        lista =[]
    else:
        cadenita=(cadenita.rstrip()).lstrip()
        for j in range(cadenita.count(' ')):
            pos = cadenita.find(' ',pos+1)
            subCa+= cadenita[inicio:pos]
            inicio+=len(subCa)+1
            lista.append(subCa)
            subCa=""
        lista.append(cadenita[inicio:len(cadenita)])
    return lista

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("           "))
print(misplit(" abc "))
print(misplit(""))