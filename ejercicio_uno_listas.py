texto_usuario = input("Introduce una frase: ")

puntos = ["."]
espacio = [" "]
comas = [","]
vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "ü"]
otros_signos = [":", ";", "?", "¿", "!", "¡"]

numero_puntos = 0
numero_espacios = 0
numero_comas = 0
numero_vocales = 0
numero_otros_signos = 0
numero_consonantes = 0

for letra in texto_usuario:
    if letra in puntos:
        numero_puntos += 1
    elif letra in espacio:
        numero_espacios += 1
    elif letra in comas:
        numero_comas += 1
    elif letra in vocales:
        numero_vocales += 1
    elif letra in otros_signos:
        numero_otros_signos += 1
    else:
        numero_consonantes += 1

print("Las puntos son {}, los espacios son {} y las comas son {}. Además, las vocales son {}, los otros signos son {} y, por último, las consonantes son {}.".format(numero_puntos, numero_espacios, numero_comas, numero_vocales, numero_otros_signos, numero_consonantes))