# Ejercico 8
# Un vendedor de una pagina de abarrotes en linea vende dos tipos de caja de cereal.
# Cornflakes de 750gr y trix 500gr.
# Escriba un programa que lea el numero de cajas cornflakes y de trix, cuyo valor debe ser introducido por el usuario.
# Despues su programa debe calcular y mostrar el total del peso ( en kilogranmos) del envio.

corn = float(input('Cuantas cajar de cornflakes necesita: '))

tri = float(input('Cuantas cajar de trix necesita: '))

total = (corn * (750/1000)) + ( tri * (500/1000))

print('El total de peso es de: ', total, 'kg')
