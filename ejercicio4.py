# Ejercicio 4 
# Crear un programa que lea el largo y el ancho de un campo de cultivo, introducido por el usuario y despliegue el área del campo en acres.
# 0.000247105 acres = 1 metro

largo = float(input ('inserta el largo de la campo en metros: '))
ancho = float(input ('inserta el ancho de la campo en metros: '))

print ('\n El area del campo es de', (largo*ancho)*0.000247  , 'Acres')

