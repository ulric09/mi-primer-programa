lista_numeros = []

elementos_dicho = 0

numero_dicho = input("Hazme una lista, que yo luego te la repito y cuento items. \n\
Cuando hayas acabado de poner elementos di listo: ")

while numero_dicho != "listo":
    lista_numeros.append(numero_dicho)
    numero_dicho = input("Dime otro número: ")
    elementos_dicho += 1
else:
    print("Perfecto. Has dicho la siguiente lista: \n\
     {} \n\
      tiene {} elementos".format(lista_numeros, elementos_dicho))
