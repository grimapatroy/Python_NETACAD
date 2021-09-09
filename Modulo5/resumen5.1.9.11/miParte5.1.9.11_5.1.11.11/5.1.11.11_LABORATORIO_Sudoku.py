# Escenario
# Como probablemente sabes, Sudoku es un rompecabezas de colocación de números jugado en un tablero de 9x9.
# El jugador tiene que llenar el tablero de una manera muy específica:
#     Cada fila del tablero debe contener todos los dígitos del 0 al 9 (el orden no importa).
#     Cada columna del tablero debe contener todos los dígitos del 0 al 9 (nuevamente, el orden no importa).
#     Cada subcuadro de 3x3 de la tabla debe contener todos los dígitos del 0 al 9.
# Si necesitas más detalles, puedes encontrarlos aquí.
# Tu tarea es escribir un programa que:
#     Lea las 9 filas del Sudoku, cada una con 9 dígitos (verifica cuidadosamente si los datos ingresados son válidos).
#     Da como salida Si si el Sudoku es válido y No de lo contrario.
# Prueba tu código utilizando los datos que te proporcionamos.
# Datos de Prueba
# Entrada de Muestra:
#                 295743861
#                 431865927
#                 876192543
#                 387459216
#                 612387495
#                 549216738
#                 763524189
#                 928671354
#                 154938672
# Salida de la Muestra:
# Yes
# Entrada de Muestra:
#                 195743862
#                 431865927
#                 876192543
#                 387459216
#                 612387495
#                 549216738
#                 763524189
#                 928671354
#                 254938671
# Salida de la Muestra
# No
# --------------------------------------------------------------------------------------------------------------------------
# while True:
#     try:
#         num = int(input("Ingrese un valor: "))
#         assert validarNum
#         break
#     except ValueError:
#         print("Vuelve a Ingresar un valor numerico")


# tablero = [[num for fila in range(9)] for columna in range(9)]
# tablero=[[0,0,0],[0,0,0],[0,0,0]]

def extraeSubMatriz(tablero,x):
    # for i
    return ''
def validaMatriz(tablero):
    return True
def extraeColumna(tablero,i):
    lista = []
    for j in range(9):
        lista.append(tablero[j][i])
    return lista
def validoColumNum(columna):
    return True if  (columna.count(1)==1 and columna.count(2)==1 and columna.count(3)==1 and columna.count(4)==1 and columna.count(5)==1 and columna.count(6)==1 and columna.count(7)==1  and columna.count(8)==1 and columna.count(9)==1) else False
def convertirListaToInt(cadena):
    lista = []
    for char in cadena:
        lista.append(int(char,10))
    return lista
def validarCadena(cadena):
    return True if  (cadena.count('1')==1 and cadena.count('2')==1 and cadena.count('3')==1 and cadena.count('4')==1 and cadena.count('5')==1 and cadena.count('6')==1 and cadena.count('7')==1  and cadena.count('8')==1 and cadena.count('9')==1) else False
fila ,columna,tablero=[],[],[]
x,i,j=0,0,0
while j<9:
    cadena = input("ingrese texto de 9 caracteres (del 0 al 9) : ")
    if ( validarCadena(cadena)):
        fila = convertirListaToInt(cadena)
        tablero.append(fila)
        j+=1
        if  j>8:
            # print("YES")
            # print(tablero)
            while i<9:
                # comparo columnas (tablero) de 9x9 que esten del 0 al 9 y no se repitan
                columna = extraeColumna(tablero,i)  #//  extraer la columna de la lista
                if validoColumNum(columna): #validoListaNum(columna) //validar lista numerica que no se repita del 0 a 9
                    i+=1
                    if i>8:
                        print("YES")
                        print(tablero)
                        #comparar columnas y filas (tablero) de 3*3 que esten del 0 al 9 y no se repitan
                        # 1mera vuelta  ( )
                        auxMatriz3_3 = extraeSubMatriz(tablero,x)
                        while x<9 and validaMatriz(auxMatriz3_3):
                            x+=1
                            auxMatriz3_3 = extraeSubMatriz(tablero,x)
                            if x>8:
                                print("YES")
                                break
                            else:
                                print("NO")
                                break
                else:
                    print("NO")
                    break
    else:
        print("NO")
        break
