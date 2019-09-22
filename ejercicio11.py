# Ejercicio 11: Eficiencia de combustible
# En los Estados Unidos, la eficiencia del combustible para vehículos se expresa normalmente en millas por galón (MPG). 
# En México, la eficiencia del combustible normalmente se expresa en litros por cien kilómetros (L / 100 km). 
# Usa tus habilidades de investigación para determinar cómo convertir de MPG a L / 100 km. 
# Luego cree un programa que lea un valor del usuario en unidades estadounidenses y muestre la eficiencia de combustible equivalente en unidades mexicanas.
# conversión 1 mpg = 235.21 l/100km, la conversión seria es 235.21/ MPG para obtener l/100km

eu = float(input('la eficiencia en Estados unidos de MPG es: '))

conversion = 235.21 / eu 

print('\n La eficiencia de combustible en Mexico es: %.2f' % conversion, 'L/100km' )


