
multiplo = int(input("¿De que número quieres saber la tabla? "))

for numero in range(0, 11):
    print("{} x {} = {}".format(multiplo, numero, numero * multiplo))
print(" ")




#1 Modificando el programa para que vaya del 5 al 15

multiplo = int(input("¿De que número quieres saber la tabla? "))

for numero in range(5, 16):
    print("{} x {} = {}".format(multiplo, numero, numero * multiplo))
print(" ")




#2 Modificando el programa para que solo muestre los resultads que sean múltiples de 2

multiplo = int(input("¿De que número quieres saber la tabla? solo te dare los numeros pares "))

for numero in range(0, 11):
    resultado = numero * multiplo
    resto = resultado % 2
    if resto == 0:
        print("{} x {} = {}".format(multiplo, numero, resultado))

print(" ")




#3 Mostrar la tabla de multiplicar invertida

multiplo = int(input("¿De que número quieres saber la tabla"))
for numero in range(10, -1, -1):
    resultado = numero * multiplo
    print("{} x {} = {}".format(multiplo, numero, resultado))
print(" ")
