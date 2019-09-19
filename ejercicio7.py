# escriba un program que lea un numero positivo (n), insetado por el usuario y despues despliegue la suma de todos los enteros desde 1 hasta n.
# Lasuma de los primeros enteros n positivos pueden ser calculando usando la formula (n)(n+1) / 2

numero = int(input('Inserte numero positivo: '))

suma = int(( numero * ( numero + 1 ))/ 2)

print('la suma de los primeros numero positivos son', suma)