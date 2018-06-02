
mi_lista  = []
input_usuario = input("¿Que necesitas comprar? ")

while input_usuario != "fin":
    mi_lista.append(input_usuario)
    input_usuario = input("¿Que necesitas comprar? ")

largo_lista = len(mi_lista)
indice_actual = 0

for item in mi_lista:
    print("Tengo que comprar {}".format(item))

print("Esta es la lista de la compra")