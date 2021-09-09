tablero=[[1,2,3,4,5,6,9,8,7],[3,6,9,8,7,5,5,8,6],[0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1],[9,8,7,6,5,4,1,3,2],[0,0,0,0,0,0,0,0,0],[0,1,7,8,2,0,3,6,5] ,[3,6,9,8,7,5,5,8,6],[9,8,7,6,5,4,1,3,2]]


def extraeMatriz(tablero,x):
    lista = []
    # i,j=0,0
    estadoIniciali = 0 if (x==0 or x==1 or x==2)  else (  3 if (x==3 or x==4 or x==5) else 6)
    estadoInicialj= 0 if x==0 else ( 3 if x==1  else 6)


    # estadoInicialj= 0 if x==0 else (  3 if x==1   else 6)
    # rango = 3 if estadoInicialj==0 else ( 6 if estadoInicialj==3 else 9 )
    rangoi =  3 if  estadoIniciali==0 else ( 6 if estadoIniciali==6 else ( 9 ) )
    rangoj= 3 if estadoInicialj==0 else ( 6 if estadoInicialj==3 else 9 )
    # rango = 3 if estadoIniciali==0 else ( 6 if estadoIniciali==3 else 9 )
    i=estadoIniciali
    j=estadoInicialj
    while i<rangoi:
        while j<rangoj:
            lista.append(tablero[i][j])
            j+=1
        j=estadoInicialj
        i+=1
    return lista
    # for i in range(3):
    #     for j in range(3):
    #     lista.insert(tablero[i][j])
    #         lista.append(tablero[i][j])
    # return lista


print(extraeMatriz(tablero,3))


# prueba = tablero[1:2:1]
# print(prueba)

# lista = []
# for i in range(1):
#     for j in range(3):
#     #  lista.insert(tablero[i][j],j)
#         # lista.append(tablero[i][j])
#         print(tablero[j][i])

# for j in range(3):
#     #  lista.insert(tablero[i][j],j)
#     # lista.append(tablero[i][j])
#     print(tablero[0][j])

# def extraeColumna(tablero,i):
#     lista = []
#     for j in range(3):
#         # lista.insert(tablero[i][j])
#         lista.append(tablero[j][i])
#     return lista