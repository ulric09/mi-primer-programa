lista_numeros = []
numero_numeros = 0

listo = input("¿Estás listo para empezar? ")
while not listo == "si":
    print("Vaya, veo que aún no estas listo")
    listo = input("¿Estas listo ya?")

else:
    print("Este programa, calculará la media de todos los números que has dicho. \n\
          Cuando has acabado de dirlos, di listo")

    numero_dicho = input("Dime el primer número:  ")
    while numero_dicho != "listo":

        if numero_dicho.isdigit():
            lista_numeros.append(int(numero_dicho))
            numero_numeros += 1
            numero_dicho = input("Dime otro número: ")

        else:
            print("Melón. te he dicho que introducieras un número.")
            numero_dicho = input("Vuelve a intentarlo: ")

    media = sum(lista_numeros) / numero_numeros

    print(lista_numeros)
    print("La media de la lista que me has dado es de {}".format(media))



