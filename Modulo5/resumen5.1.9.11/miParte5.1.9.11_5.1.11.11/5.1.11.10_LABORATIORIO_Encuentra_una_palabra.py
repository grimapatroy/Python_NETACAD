# Objetivos
#     Mejorar las habilidades del alumno para trabajar con cadenas.
#     Emplear el método find() para realizar busquedas dentro de las cadenas.
# Escenario
# Vamos a jugar un juego. Le daremos dos cadenas: una es una palabra (por ejemplo, "dog")
# y la segunda es una combinación de un grupo de caracteres.
# Tu tarea es escribir un programa que responda la siguiente pregunta: ¿Los caracteres que
# comprenden la primera cadena están ocultos dentro de la segunda cadena?
# Por ejemplo:
#     Si la segunda cadena es "vcxzxduybfdsobywuefgas", la respuesta es si.
#     Si la segunda cadena es "vcxzxdcybfdstbywuefsas", la respuesta es no
#     (ya que no están las letras "d", "o", "g", ni en ese orden).
# Consejos:
#     Debes usar las variantes de dos argumentos de las funciones pos()
#     dentro de tu código.
#     No te preocupes por mayúsculas y minúsculas.
# Prueba tu código utilizando los datos que te proporcionamos.
# Datos de Prueba
# Entrada de Ejemplo:
# donor
# Nabucodonosor
# Salida del Ejemplo:
# Si
# Entrada de Ejemplo:
# donut
# Nabucodonosor
# Salida del Ejemplo:
# No

palabra=input("Ingrese una palabra: ")
texto=input("Ingrese un texto: ")

cant = len(palabra)
for char1 in palabra:
    pos = texto.find(char1,0)
    if pos>-1:
        cant-=1
        continue
if cant==0:
    print("SI")
else:
    print("NO")
