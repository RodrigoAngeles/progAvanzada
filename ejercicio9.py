# Usted acaba de abrir una nueva cuantra de ahorros con el cual gana el 4% de interes por año.
# el interes que usted genera es pagado al final del año y es agregado al balnace de la cuenta de banco.
# Escriba un un programa que comince por leer la cantidad de dinero depositada en la cuenta ( el usuario introduce esa cantidad).
# el programa debe calcular y mostrar la cantidad de dinero en la cuenta despues del primer, segundo y tercer año. 
#despliege las cantidades de dinero redondeando a 2 decimales.

cantidad =  float(input('Cuanto dinero depocitara: '))

ano1 = ((cantidad * 0.04) + cantidad)

ano2 = ((ano1 * 0.04) + ano1)

ano3 = ((ano2 * 0.04) + ano2)

print('\n En el año 1 la cantidad es de: $%.2f' %ano1)

print('\n En el año 2 la cantidad es de: $%.2f' %ano2)

print('\n En el año 3 la cantidad es de: $%.2f' %ano3)
