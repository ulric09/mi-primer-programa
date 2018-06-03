lista_numeros = []

while len(lista_numeros) < 5:
    numero_dicho = input("Dime el siguiente número: ")
    if numero_dicho.isdigit():
        lista_numeros.append(int(numero_dicho))
    else:
        print("Esto no es un número, melón")

numero_pequeño = lista_numeros[0]

for numero in lista_numeros:
    if numero_pequeño > numero:
        numero_pequeño = numero

print("El número más pequeño es {}".format(numero_pequeño))
