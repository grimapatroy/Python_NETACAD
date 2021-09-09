# Objetivos
#     Mejorar las habilidades del alumno para manipular cadenas.
#     Convertir caracteres en código ASCII y viceversa.
# Escenario
# Ya estás familiarizado con el cifrado César, y es por eso que queremos que mejores el código
# que te mostramos recientemente.

# El cifrado César original cambia cada caracter por otro a se convierte en b, z se convierte en a,
# y así sucesivamente. Hagámoslo un poco más difícil y permitamos que el valor desplazado provenga
# del rango 1 al 25.
# Además, dejemos que el código conserve las mayúsculas y minúsculas (las minúsculas permanecerán en
# minúsculas) y todos los caracteres no alfabéticos deben permanecer intactos.
# Tu tarea es escribir un programa el cual:

#     Le pida al usuario una línea de texto para encriptar.
#     Le pida al usuario un valor de cambio (un número entero del rango 1 al 25, nota: debes obligar
#     al usuario a ingresar un valor de cambio válido (¡no te rindas y no dejes que los datos incorrectos
#     te engañen!).
#     Imprime el texto codificado.
# Prueba tu código utilizando los datos que te proporcionamos.
# Datos de Prueba

# Entrada Muestra:
# abcxyzABCxyz 123
# 2

# Salida Muestra:
# cdezabCDEzab 123

# Entrada Muestra:
# The die is cast
# 25

# Salida Muestra:
# Sgd chd hr bzrs



text = input("Ingresa tu mensaje: ")
cifrado=""
code=0
while True:
    try:
        vCambio= int(input("Ingrese un valor de cambio(del 1 al 25): "))
        assert (vCambio>0 and vCambio<=25)
        break
    except ValueError:
        print("Valor Ingresado Erroneo, Vuelva a ingresar valor de cambio")
    except AssertionError:
        print("Valor fuera del rango, vuela a ingresar valor de 1 a 25","*"*100,sep="\n")

for char in text:
    if  char.isalpha():
        if (ord(char)>=65 and ord(char)<=90):
            code = ord(char)+vCambio
            if code > 90:
                code = 65+(vCambio - (90-ord(char))  -1)
        if (ord(char)>=97 and ord(char)<=122):
            code = ord(char)+vCambio
            if code > 122 :
                code = 97 + (vCambio - (122-ord(char))  -1)
    cifrado+= char if (char.isdigit() or char.isspace()) else chr(code)
print(cifrado)