# Ejercicio 8
# Un vendedor de una página de abarrotes en línea vende dos tipos de caja de cereal.
# Cornflakes de 750gr y trix 500gr.
# Escriba un programa que lea el número de cajas cornflakes y de trix, cuyo valor debe ser introducido por el usuario.
# Después su programa debe calcular y mostrar el total del peso (en kilogramos) del envió.


corn = float(input('Cuantas cajar de cornflakes necesita: '))

tri = float(input('Cuantas cajar de trix necesita: '))

total = (corn * (750/1000)) + ( tri * (500/1000))

print('El total de peso es de: ', total, 'kg')
