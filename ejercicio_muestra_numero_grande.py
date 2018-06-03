lista_numeros = []
numero_dicho = ""

while len(lista_numeros) < 10 :
    numero_dicho = input("¿Cual es el siguiente número?")
    if numero_dicho.isdigit():
        lista_numeros.append(numero_dicho)
    else:
        print("Esto no es un número. Por favor, vuelve a intentarlo: ")
print(lista_numeros)

numero_mayor = lista_numeros[0]
for numero in lista_numeros:
    if numero_mayor < numero:
        numero_mayor = numero
    else:
        print("El número era más pequeño")


print("El número más grande que has puesto es {}".format(numero_mayor))







