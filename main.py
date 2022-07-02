# El ejercicio consiste en crear un programa que muestre por consola la carta de un restaurante donde añadiremos
# diferentes platos y después escogeremos que queramos para comer. Una vez hecho esto se tendrá que calcular el
# precio de la comida, el programa nos tiene que decir con qué billetes y monedas tenemos que pagar.

precio_total = 0
Menu = []  # Array o matriz para el Menú
Precio = []  # Array o matriz para los precios
dic = {}  # Diccionario para consultar precios por cada elemento del menú
t = ''  # Variable para salir de bucles
opt = 0  # Variable de opción
milista = []  # Lista donde apuntar los pedidos

for element in range(20):  # Permitimos la introducción de hasta 20 platos (Puede ser ampliable en cuanto al rango)
    Menu.append(input("Introduce el plato número " + str(element+1) + ": "))
    Precio.append(input("Introduce el precio para el plato en euros (€): "))
    dic.update({Menu[element]: Precio[element]})  # Añadimos los elementos al diccionario
    t = input("Pulse la tecla 's' para introducir más platos, para salir pulse cualquier otra tecla: ")
    if t != 's':
        break  # Si pulsamos cualquier otra tecla que no sea 's' dejaremos de introducir platos
print("Por favor, seleccione de entre las opciones del menú lo que desee consumir")
for element in range(len(Menu)):
    print(str(Menu[element] + " , Precio: " + Precio[element] + "€"))

while True:
    milista.append(input("Introduzca lo que desea comer: "))
    for e in milista:
        if e not in Menu:
            print("El plato seleccionado no está en nuestro menú")
            milista.pop()  # Borramos o tachamos de la lista el pedido no existente en nuestro menú
            print("Su pedido es: " + str(milista))
    t = input("¿Desea seleccionar más platos? Si (s) / No (otra tecla): ")
    if t != 's':
        break  # Si la opción es distinta de 's' habremos acabado de hacer el pedido y saldremos del loop
    else:
        continue
for e in milista:
    print(e + ": " + dic.get(e) + " €")  # Consultamos el diccionario para saber el precio de cada plato de la lista
    precio_total += int(dic.get(e))
print("Precio total: " + str(precio_total) + " €")

monedas_de_1 = precio_total
billetes_de_500 = (monedas_de_1-monedas_de_1 % 500)//500
monedas_de_1 = monedas_de_1 % 500
billetes_de_200 = (monedas_de_1-monedas_de_1 % 200)//200
monedas_de_1 = monedas_de_1 % 200
billetes_de_100 = (monedas_de_1-monedas_de_1 % 100)//100
monedas_de_1 = monedas_de_1 % 100
billetes_de_50 = (monedas_de_1-monedas_de_1 % 50)//50
monedas_de_1 = monedas_de_1 % 50
billetes_de_20 = (monedas_de_1-monedas_de_1 % 20)//20
monedas_de_1 = monedas_de_1 % 20
billetes_de_10 = (monedas_de_1-monedas_de_1 % 10)//10
monedas_de_1 = monedas_de_1 % 10
billetes_de_5 = (monedas_de_1-monedas_de_1 % 5)//5
monedas_de_1 = monedas_de_1 % 5
monedas_de_2 = (monedas_de_1-monedas_de_1 % 2)//2
monedas_de_1 = monedas_de_1 % 2
print('Monedas de 1: ' + str(monedas_de_1))
print('Monedas de 2: ' + str(monedas_de_2))
print('Billetes de 5: ' + str(billetes_de_5))
print('Billetes de 10: ' + str(billetes_de_10))
print('Billetes de 20: ' + str(billetes_de_20))
print('Billetes de 50: ' + str(billetes_de_50))
print('Billetes de 100: ' + str(billetes_de_100))
print('Billetes de 200: ' + str(billetes_de_200))
print('Billetes de 500: ' + str(billetes_de_500))
