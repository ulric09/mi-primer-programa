
lista_inicial = [1, 2, 3, "gato", "perro", True]

lista_enteros = []

lista_booleanos = []

lista_string = []

for elemento in lista_inicial:

    if type(elemento) == int:
        lista_enteros.append(elemento)
    elif type(elemento) == bool:
         lista_booleanos.append(elemento)
    elif type(elemento) == str:
        lista_string.append(elemento)


print(lista_enteros, lista_string, lista_booleanos)
