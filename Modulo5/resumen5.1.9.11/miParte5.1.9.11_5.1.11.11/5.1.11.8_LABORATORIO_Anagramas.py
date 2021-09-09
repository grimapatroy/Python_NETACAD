# Un anagrama es una nueva palabra formada al reorganizar las letras de una palabra, usando
# todas las letras originales exactamente una vez. Por ejemplo, las frases "rail safety" y
# "fairy tales" son anagramas, mientras que "I am" y "You are" no lo son.
# Tu tarea es escribir un programa que:
#     Le pida al usuario dos textos por separado.
#     Compruebe si los textos ingresados son anagramas e imprima el resultado.
# Nota:
#     Supongamos que dos cadenas vacías no son anagramas.
#     Tratar las letras mayúsculas y minúsculas como iguales.
#     Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.

# Datos de Prueba
# Entrada de Ejemplo:
# Listen
# Silent
# Salida del Ejemplo:
# Anagramas
# Entrada de Ejemplo:
# modern
# norman
# Salida del Ejemplo:
# No son Anagramas

def eliminarSpace(cadena):
    cadenita=""
    for char in cadena:
        if char.isspace():
            continue
        cadenita +=char
    return cadenita

text1 = input("Ingrese el texto uno: ")
text2 = input("Ingrese el texto dos: ")
text1=text1.lower()
text2=text2.lower()

# rail safety
# fairy tales
lista = []
for char1 in text1:
    aparece = text1.count(char1)
    completo=False
    if aparece > 0 and  not char1.isspace():
        for char2 in text2:
            if  not char2.isspace():
                if char1 == char2:
                    aparece-=1

                # resto = aparece
                if aparece ==0:
                    completo = True
                    if  completo:
                        lista.append(char2)
                    break
            else:
                continue
    else:
        continue

resultado =   print("ES UN ANAGRAMA")   if  (len(eliminarSpace(text1))==len(lista) and len(eliminarSpace(text2))==len(lista) )  else print("NO ES UN ANAGRAMA")
