from sys import path

# ruta relativa
path.append('..\\packages')
import extra.iota as Mostar
import ugly.omega as cal1
import ugly.psi as cal2
from good import beta as string

op1=(int(input("Introduce el primer nomero: ")))

op2=(int(input("Introduce el segundo nomero: ")))

operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(cal2.suma(op1,op2))

elif operacion=="resta":
	print(cal2.resta(op1,op2))

elif operacion=="multiplica":
	print(cal2.multiplica(op1,op2))

elif operacion=="divide":
	print(cal2.divide(op1,op2))

else:
	print ("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecocion del programa ")