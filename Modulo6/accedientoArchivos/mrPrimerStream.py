try:
    stream = open("C:\\Users\\Humanitroy\\Desktop\\file.txt", "rt")
    # aqui se procesa el archivo
    print(stream.read()) # se imprime el contenido del archivo
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo:", exc)