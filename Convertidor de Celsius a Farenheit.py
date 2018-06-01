necesita_calculo = input("¿Tienes que hacer alguna conversión, hoy (si / no) :?")

while necesita_calculo == "si":

    escala_a_convertir = input("¿Que quieres conocer, celsius o farenheit?")
    temoeratura_a_convertir = int(input("Cuál es la temperatura que quieres convertir?"))

    if escala_a_convertir == "celsius":
        resultado_en_celsius = (temoeratura_a_convertir - 32)/1.8
        print("La temperatura en Celsius es {} grados".format(resultado_en_celsius))
        necesita_calculo = input("¿Necesitas otro cálculo?")

    elif escala_a_convertir == "farenheit":
        resultado_en_farenheit = (temoeratura_a_convertir *1.8) +32
        print("La temperatura en Farenheit es de {} grados".format(resultado_en_farenheit))
        necesita_calculo = input("¿Necesitas otro cálculo?")
    else:
        print("No has introducido bien los datos, mamonazo")

print("Gracias por usar este convertidor interactivo")
