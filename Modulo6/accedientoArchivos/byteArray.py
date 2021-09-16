from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open("C:\\Users\\Humanitroy\\Desktop\\file.txt", "wb")
    bf.write(data)
    bf.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

    # ingresa aquí el código que lee los bytes del stream
try:
    bf = open("C:\\Users\\Humanitroy\\Desktop\\file.txt", "rb")
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))


# /////////////////////////////////////////////////////////////////////////////
from os import strerror

try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))