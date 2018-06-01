numero_adivinar = int(input("¿Que numero quieres que Juanito adivine? Shht, que no lo vea!: "))
numero_dicho = None

while numero_dicho != numero_adivinar:
    numero_dicho = int(input("Adivina, adivinanza... ¿Qué número tengo en la panza?: "))

    if numero_dicho == numero_adivinar:
        print("Eres un mentalista... fenoómeno, tifón, mastodonete, Hulk")
    else:
        print("Eres un parguelilla... Pero me caes bien, te doy más oportunidades")
