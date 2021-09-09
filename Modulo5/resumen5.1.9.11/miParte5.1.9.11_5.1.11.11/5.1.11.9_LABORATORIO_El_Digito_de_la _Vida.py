# Objetivos
#     Mejorar las habilidades del alumno para trabajar con cadenas.
#     Convertir enteros en cadenas, y viceversa.
# Escenario
# Algunos dicen que el Dígito de la Vida es un dígito calculado usando el cumpleaños de alguien.
# Es simple: solo necesitas sumar todos los dígitos de la fecha. Si el resultado contiene
# más de un dígito, se debe repetir la suma hasta obtener exactamente un dígito. Por ejemplo:
#     1 Enero 2017 = 2017 01 01
#     2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
#     1 + 2 = 3
# 3 es el dígito que buscamos y encontramos.
# Tu tarea es escribir un programa que:
#     Le pregunta al usuario su cumpleaños (en el formato AAAAMMDD o AAAADMM o MMDDAAAA; en realidad,
#     el orden de los dígitos no importa).
#     Da como salida El Dígito de la Vida para la fecha ingresada.
# Prueba tu código utilizando los datos que te proporcionamos.
# Datos de Prueba
# Entrada de Ejemplo:
# 19991229
# Salida del Ejemplo:
# 6
# Entrada de Ejemplo:
# 20000101
# Salida del Ejemplo:
# 4

def sumaDigit(cadena):
    numVida=0
    for char in cadena:
        numVida+= int(char,10)
    return numVida



fecha = input("INGRESE SU FECHA aa/mm/dd: ")
numVida=sumaDigit(fecha)
resultado = print(sumaDigit(str(numVida))) if numVida>10 else numVida