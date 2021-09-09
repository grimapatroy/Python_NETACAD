class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val


objetoPila = Pila()

objetoPila1 = Pila()
objetoPila2 = Pila()



objetoPila1.push(3)
objetoPila.push(3)
objetoPila.push(2)
objetoPila.push(1)
objetoPila2.push(objetoPila1.pop())

print(objetoPila.pop())
print(objetoPila.pop())
print(objetoPila.pop())
print(objetoPila2.pop( ))

pequeñaPila = Pila()
otraPila = Pila()
graciosaPila = Pila()

pequeñaPila.push(1)
otraPila.push(pequeñaPila.pop() + 1)
graciosaPila.push(otraPila.pop() - 2)

print(graciosaPila.pop())