from os import strerror

# try:
#     cnt = 0
#     s = open("C:\\Users\\Humanitroy\\Desktop\\file.txt", "rt")
#     ch = s.read(1)
#     while ch != '':
#         print(ch, end='')
#         cnt += 1
#         ch = s.read(1)
#     s.close()
#     print("\n\nCaracteres en el archivo: ", cnt)
# except IOError as e:
#     print("Se produjo un error de E/S: ", strerror(e.errno))

from os import strerror

try:
    cnt = 0
    s = open("C:\\Users\\Humanitroy\\Desktop\\file.txt", "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCaracteres en el archivo: ", cnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

