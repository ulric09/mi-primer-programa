texto_usuario = "Hola, me llamo Ulric. ¿Tu como te llamas?"
lista_de_vocales = []

for letras in texto_usuario:
    if letras == "a":
        lista_de_vocales.append("a")
    elif letras == "e":
        lista_de_vocales.append("e")
    elif letras == "i":
        lista_de_vocales.append("i")
    elif letras == "o":
        lista_de_vocales.append("o")
    elif letras == "u":
        lista_de_vocales.append("u")

print(lista_de_vocales)