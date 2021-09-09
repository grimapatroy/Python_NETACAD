def readint(a, min, max):
    
    try:
        if a.isdecimal() and int(a,10)<=0 :
            a=int(a,10)
            if (a>min and a>max):
                raise ArithmeticError
        if type(a) == str  and a.isdigit()==False:
            raise ValueError
    except ValueError:
        print("Error: entrada incorrecta")
    except ArithmeticError:
        print("Error: el valor no está dentro del rango permitido (-10..10)")
    # return "" if (not AssertionError and not ArithmeticError) else a
    return a

v = readint(input("Ingresa tres numero de -10 a 10: "),-10,10)

# a=int("-10",10)
# print(type(a)==str)
# print(a)

# while True:
#     try:
#         v = readint("Ingresa un 5numero de -10 a 10: ", -10, 10)
#         break
#     except ValueError:
#         print("Error: entrada incorrecta")


print("El numero es:", v)