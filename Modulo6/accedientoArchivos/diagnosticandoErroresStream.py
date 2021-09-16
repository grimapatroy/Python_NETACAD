import errno
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # el procesamiento va aquí
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("El archivo no existe.")
    elif exc.errno == errno.EMFILE:
        print("Has abierto demasiados archivos.")
    else:
        print("El número de error es:", exc.errno)


# Afortunadamente, existe una función que puede simplificar el código de manejo de errores. Su nombre es strerror(), y proviene del módulo os y espera solo un argumento: un número de error.
# Nota: Si pasas un código de error inexistente (un número que no está vinculado a ningún error real), la función lanzará una excepción ValueError.
# Ahora podemos simplificar nuestro código de la siguiente manera:

from os import strerror
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # el procesamiento va aquí
    s.close()
except Exception as exc:
    print("El archivo no se pudo abrir:", strerror(exc.errno));