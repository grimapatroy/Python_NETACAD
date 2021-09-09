# El cifrado César: descifrando un mensaje
# La operación inversa ahora debería ser clara para ti: solo presentamos el código tal como está,
# sin ninguna explicación.
# Observa el código en el editor. Comprueba cuidadosamente si funciona. Usa el criptograma del
# programa anterior.


# Cifrado César - descifrar un mensaje
cifrado = input('Ingresa tu criptograma: ')
text = ''
for char in cifrado:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)