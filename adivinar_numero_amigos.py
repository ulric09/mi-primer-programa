listo_para_jugar = input("¿Quieres empezar la partida ya? si / no")
if listo_para_jugar == "si":
    numero_adivinar = int(input("¿Cúal es el número que quieres que tu amigo adivine?: "))
    numero_expresado = int(input("Parguelilla, ¿Que número crees que es?"))

    while listo_para_jugar == "si":

        if numero_adivinar != numero_expresado:
            print("Parguelilla, has fallado!!, tienes más oportunidades")
            numero_expresado = int(input("Otra vez... ¿Que número crees que es?"))
        else:
            print(" Adivinaste!!, Gracias por jugar!!")
            listo_para_jugar = input("¿Repetimos?")

            if listo_para_jugar == "si":
                numero_adivinar = int(input("¿Cúal es el número que quieres que tu amigo adivine?: "))
                numero_expresado = int(input("Parguelilla, ¿Que número crees que es?"))
            else:
             print("Vaya...")

print("¡Gracias por jugar!. chao chao")
