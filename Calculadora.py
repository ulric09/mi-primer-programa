continuar_calculando = input("¿Tienes algun cáclculo por hacer hoy? si o no: ")
if continuar_calculando == "si":
    while continuar_calculando == "si":
        estas_listo = input("¿Estas listo? si o no:  ")
        if estas_listo == "si":
            print("¡Adelante, empecemos!")
            calculo_necesitado = input("¿escoge entre multiplicar, dividir, sumar o restar: ")
            primer_numero = int(input("Primer número: "))
            segundo_numero = int(input("Segundo número: "))

            if calculo_necesitado == "sumar":
                resultado_suma = primer_numero + segundo_numero
                print("El resultado es {}".format(resultado_suma))
                print("¡Gracias por utilizar la calculadora interactiva!")

            elif calculo_necesitado == "multiplicar":
                resultado_multiplicacion = primer_numero * segundo_numero
                print("El resultado es {}".format(resultado_multiplicacion))
                print("¡Gracias por utilizar la calculadora interactiva!")

            elif calculo_necesitado == "dividir":
                resultado_division = primer_numero / segundo_numero
                print("El resultado es {}".format(resultado_division))
                print("¡Gracias por utilizar la calculadora interactiva!")

            elif calculo_necesitado == "restar":
                resultado_resta = primer_numero - segundo_numero
                print("El resultado es {}".format(resultado_resta))
                print("¡Gracias por utilizar la calculadora interactiva!")
            else:
                print("Upss!! Algo ha fallado... ¿Has indicado bien el cálculo y/o los números? De todos modos, aunque seas cazurro, igual te queremos. Gracias por usar la calculadora interactiva")
else:
    print("Gracias por usar la calculadora interactiva")



