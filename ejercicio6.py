# hacer un programa en el que el usuario introduzca el nombre de la comida que ordeno en un restaurante y su precio. 
#Despues su programa debe calcular el subtotal, el iva y la propina, de toda la cuenta. 
#la salida del programa deve parecerse a un tiquet de restrurante. use un iva del 16% y una propina del 15% del subtotal.
#los valores nujmericos deven tener 2 decimales

comida1 = input ('introduzca el nombre de la comida: ')
valor1 = float(input ('Intruduzca el valor de la comida: '))
comida2 = input ('introduzca el nombre de la comida: ')
valor2 = float(input ('Intruduzca el valor de la comida: '))
comida3 = input ('introduzca el nombre de la comida: ')
valor3 = float(input ('Intruduzca el valor de la comida: '))
comida4 = input ('introduzca el nombre de la comida: ')
valor4 = float(input ('Intruduzca el valor de la comida: '))
comida5 = input ('introduzca el nombre de la comida: ')
valor5 = float(input ('Intruduzca el valor de la comida: '))

Subtotal = valor1 + valor2 + valor3 + valor4 + valor5
Iva = Subtotal * 0.16 
Propina = Subtotal * 0.15 
Total = Subtotal + Iva + Propina

print('\n subtotal:      $%.2f.' % Subtotal)
print('\n iva:           $%.2f.' % Iva)
print('\n propina:       $%.2f.' % Propina )
print('\n -----------------------')
print('\n total:         $%.2f.' % Total)