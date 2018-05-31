apetece_helado_input = input("Te apetece un helado? (Si/No): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Te he dicho que me digas si o no; toooooonto!")
    apetece_helado = False

tienes_dinero_input = input("Tienes dinero para un helado? (Si/no): ").upper()
esta_el_senor_helados_input = input("Esta el señor de los helados? (Si/no): ").upper()
esta_tu_tia_input = input("Estas con tu tia?: ").upper()


apetece_helado = apetece_helado_input == "SI"
puedes_permitirtelo = tienes_dinero_input == "SI" or esta_tu_tia_input == "SI"
esta_el_senor_helados = esta_el_senor_helados_input == "SI"

if apetece_helado and puedes_permitirtelo and esta_el_señor_helados:
    print("Palante, engorda")
else:
    print("Te jodes, a comer acelgas")
