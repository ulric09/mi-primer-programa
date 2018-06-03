texto_usuario = input( "Por favor, introduce la frase en la que quieras contar las mayúsculas: ")

mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numero_mayusculas = 0
resto = 0

for letra in texto_usuario:
    if letra in mayusculas:
        numero_mayusculas += 1
    else:
        resto += 1

print("El número de mayúculas es de {}. Todo lo demas es {}".format(numero_mayusculas, resto))

