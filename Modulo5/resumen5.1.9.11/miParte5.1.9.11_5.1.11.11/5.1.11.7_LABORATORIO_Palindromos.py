# ¿Sabes qué es un palíndromo?
# Es una palabra que se ve igual cuando se lee hacia adelante y hacia atrás. Por ejemplo,
#  "kayak" es un palíndromo, mientras que "leal" no lo es.
# Tu tarea es escribir un programa que:
#     Le pida al usuario algún texto.
#     Compruebe si el texto introducido es un palíndromo e imprima el resultado.
# Nota:
#     Supón que una cadena vacía no es un palíndromo.
#     Trata las letras mayúsculas y minúsculas como iguales.
#     Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.
#     Existe más de una solución correcta: intenta encontrar más de una.
# Datos de Prueba
# Entrada Muestra:
# Ten animals I slam in a net
# Salida Muestra:
# Es un palíndromo
# Entrada Muestra:
# Eleven animals I slam in a net
# Salida Muestra:
# No es un palíndromo


# text = input("Ingrese algun texto: ")
while True:
    try:
        text = input("Ingrese algun texto: ")
        assert  (not text.isspace())==True
        break
    except ValueError:
        print("Ingrese solo letras, vuelva a ingresar")
    except AssertionError:
        print("Las cadadenas vacias no son palidromos, vuelva ingresar")

# validar cadeba vacia no es palindromo
text = text.lower()
i = len(text)-1
for char in (text):
    if char.isspace():
        continue
    if text[i].isspace():
        i-=1
    if(char == text[i] and i>=0):
        i-=1
print("ES PALINDROMO") if i==-1 else print("No es palindromo")