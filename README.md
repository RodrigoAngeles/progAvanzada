# Programación Avanzada
## Introducción

### ¿Qué es Python?
Es un lenguaje de programación creado por Guido Van Rossum, a principios de los años 1990. El lenguaje favorece una sintaxis muy limpia, ya que favorece un código legible, se trata de un lenguaje interpretador o de script, con tipado dinámico, fuertemente tipado, multiplataforma y orientado a objetos.

### El lenguaje interpretador o de script
Es aquel que se ejecuta utilizando un programa intermedio llamado interprete, en lugar de copilar el código el lenguaje máquina que pueda comprender y ejecutar directamente una computadora (lenguaje copilado) la ventaja de los lenguajes copilado es que su ejecución es más rápida. Sin embargo, los lenguajes interpretados son más flexibles y más portables. Python es un ejemplo de lenguaje de alto nivel como: C++, C#, PHP, Pascal y Java.
Lenguajes de bajo nivel se refiere a los lenguajes maquina o lenguajes de ensamblador, sin embargo, los lenguajes de alto nivel siempre tienen que ser convertidos a lenguaje de bajo nivel para que pueda correr.
El lenguaje de programación Python guarda sus archivos con la extensión .py
### Tipado dinámico
Se refiere a que no es necesario declarar el tipo de dato que va a contener determinada variable, sino que su tipo se determina en el tiempo de ejecución según el tipo de valor al que se asigna y al tipo de esta variable se puede cambiar si se le asigna un valor de otro tipo
### Fuertemente tipado
No se permite tratar a una variable como si fuera de un tipo distinto al que tiene, es necesario convertir al nuevo tipo previamente, por ejemplo. Si tenemos un variable que contiene un texto (Variable de tipo cadena o string) no podemos tratarla como un número (sumar la cadena “9” + “8”) 
### Multiplataforma
El intérprete de Python está disponible en multitud de catálogos (Unix, Solaris, Linux, Dos, Windows, OS/2, Mac OS, Android) por lo que si no utilizamos librerías específicas de cada plataforma podrá correr sin grandes cambios.
### Orientado a objetos
La orientación a objetos es un paradigma de programación en el que los conceptos del mundo real relevante para nuestro problema se trasladan a clases y objetos. La ejecución del programa consiste en una serie de interacción entre los objetos.
### El software 
Es núcleo de todas las herramientas que utilizamos hoy en día: casi todos usamos redes sociales para comunicarnos, muchas personas están conectadas a internet todo el día y la mayoría de los trabajos siempre se interactúa con una computadora para tener el trabajo hecho. Como resultado la demanda de las personas que sepan programar ha aumentado.
### ¿Por qué Python?
Python es el lenguaje que su sintaxis simple, clara y sencilla puede automatizar tareas como: Mover y renombrar miles de archivos y clasificarlos en folder, llenar de forma automática formatos de internet, descargar archivos o extraer formatos de páginas de internet de forma masiva, hacer que la computadora envié información al teléfono de quien la está usando, checar el email y contestar de forma automática.


## Ejercicio 1

En el ejercicio 1 se aprendió a utilizar los comandos que se ingresan en el editor de texto en el cual se le dará la instrucción de “imprimir” las frases o palabras que le hayamos escrito, ya que se hizo lo anterior, se guardara el archivo con la extensión “.py” que es la extensión que se usara con la aplicación de anaconda. También en este ejercicio 1 se aprendió a utilizar los comandos, pero para PYTHON PROMPT, en donde se le va indicar en que carpeta se tiene guardado ese archivo creado con la extensión “.py” 
Conociendo los pasos anteriores, se procedió a realizar el ejercicio 1 que consistió en realizar una carta indicando el destinatario y el remitente.

[Ejercicio 1](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio1.py)

## Ejercicio 2

En este ejercicio se aprendió un nuevo comando, con el cual el programa le pregunte al usuario su nombre, para realizar esto se hizo uso del comando “input” al poner este comando el programa permite introducir palabras por ejemplo un nombre propio que es el caso del ejercicio 2, donde se le indica al programa que pregunte por el nombre del usuario, y el usuario al poner el nombre, la maquina le contesta con un hola bienvenido seguido del nombre del usuario.

[Ejercicio 2](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio2.py)

## Ejercicio 3

Para la realización de este ejercicio utilizamos un nuevo comando, el cual le pregunta al usuario un numero entero con punto decimal, para la realización de esta indicación se hace uso del comando “float” con el cual se podrá introducir un numero con punto decimal, también se hizo uso de una pequeña formula de multiplicación, ya que el objetivo de este programa es indicar el largo y ancho de una habitación, para realizar la multiplicación solo se hace uso de un “ * ” el cual le indica al programa que se trata de una multiplicación. Ya indicado lo anterior el programa responde al usuario el área de la habitación en metros cuadrados.

[Ejercicio 3](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio3.py)

## Ejercicio 4

Para la realización de este ejercicio se hizo uso de lo aprendido en el ejercicio 3, solo que en este caso el usuario indicara al programa el largo y ancho de un campo de cultivo en metros, lo que el programa debe realizar es una conversión de unidades, pasando de metros a acres, para la realización de la conversión se necita saber cuánto equivale 1 metro a acress, el cual es 1 m = 0.000247105 acres. Por ultimo simplemente se le indica al programa que realiza la siguiente ecuación:
(largo * ancho) * 0. 0.000247105

[Ejercicio 4](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio4.py)

## Ejercicio 5

Para la realización de este ejercicio se hizo uso simplemente de dos multiplicaciones y una suma, en este programa se realiza el intercambio de botellas plásticas por dinero (botellas de menos de un litro equivalen a $0.10 y botellas de más de un litro equivale a $0.25), se tiene que ingresar al programa un numero de botella de menos de 1 litro y el número de botellas de más de 1 litro, al ingresar la cantidad de botellas, el programa calcula cuantas botellas se ingresan y suma los resultados dando una sola cantidad generada.

[Ejercicio 5](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio5.py)

## Ejercicio 6
Para este programa el usuario deberá de indicar a el programa el nombre de la comida que ordeno seguido del precio de esta, en un total de 5 comidas a pedir, El programa deberá realizar la función de calcular el subtotal, el IVA, la propina y el total a pagar, estas cantidades deberán aparecer en la pantalla como en un ticket real, poniendo en columnas separadas las cantidades que se están cobrando y finalizando con el total a pagar.

[Ejercicio 6](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio6.py)

## Ejercicio 7
Para este programa se realizará la función de ingresar un número positivo cualquiera, y el programa desplegará la cantidad de números enteros desde 1, indicando como resultado todos los números posibles enteros con esa cantidad.
Para calcular los numero se hace uso de la formula (n (n + 1)) / 2

[Ejercicio 7](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio7.py)

## Ejercicio 8
En este ejercicio se realiza la suma en kilogramos de 2 cereales distintos a vender, el primer cereal pesa 750gr y el segundo cereal pesa 500gr, el usuario le indita al programa cuantas cajas de cada cereal necesita, y el programa realiza la función de convertir los gr a kg, y sumando las cantidades de cada uno para obtener un total final.

[Ejercicio 8](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio8.py)

## Ejercicio 9
Este ejercicio trata de realizar la suma de las ganancias de una cuenta de ahorro en la cual se hizo un solo deposito obteniendo como ganancia el 4% anual, para la realización de este programa en el año uno se obtendrá una ganancia del 4% a lo depositado, esta ganancia obtenida se suma a lo depositado, para el año dos esa cantidad resultante se obtiene el 4% para adjuntarlo a lo obtenido del año 1 y por último en el año 3 la cantidad total obtenía del año 2 se saca el 4% y se suma a lo acumulado de los años anteriores danto el total ganado en esos 3 años.

[Ejercicio 9](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio9.py)

## Ejercicio 10
Para este ejercicio se debe crear un programa que lea dos números enteros, a y b, introducidos por el usuario y el programa debe calcular lo siguiente:
• La suma de a y b
• La diferencia cuando a es sustraído de b
• El producto de a y b.
• El cociente cuando a divide a b.
• El residuo cuando a divide a b.
• El resultado de log (a).
• El resultado de a, a la potencia de b.
Para poder usar el Log es necesario llamar una librería llamada math y de ahí importar Log, esto permite al programa procesar ese cálculo.
Esta librería se pone el principio de comenzar a realizar la programación de esta manera: 
from math import log 

[Ejercicio 10](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio10.py)


## Ejercicio 11

En este programa se realizará una sencilla conversión de unidades, En estados unidos la eficiencia de combustible se mide en millas por galón (MPG), mientras que en México su unidad es litro por 100 Km (l/100km), investigando se obtiene que 1 MPG es equivalente a 235.21 l/100km y 1 l/100km es equivalente a 1 MPG, por lo tanto, la fórmula para convertir MPG a l/100km es: 235.21/MPG,  entonces la función del programa consiste en que el usuario introducirá la eficiencia en MPG, y el programa realizará la conversión a l/100km.

[Ejercicio 11](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio11.py)

## Ejercicio 12
Para la realización de este programa se hizo uso de las librerías de Python denominadas math, ya que con estas hace posible realizar cálculos un poco complejos en el en el programa a realizar facilitando su uso, el programa a realizar tiene como objetivo que el usuario ingrese 2 distancias en la tierra (t1,g1) y (t2,g2), haciendo uso de la latitud y la longitud, el programa tiene que convertir los valores introducidos por el usurario que están grados a radiales ya que el programa Python solo trabaja en radianes, esto se debe de realizar antes de hacer uso de la siguiente formula que permite obtener los datos de las distancias en kilómetros.
distancia = 6271.01*arccos(sen(t1)*sen(t2)+cos(t1)*cos(t2)*cos(g1-g2))

[Ejercicio 12](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio12.py)

## Ejercicio 13
Considere el software que se ejecuta en una máquina de autopago. Una tarea que debe ser capaz de realizar es determinar cuánto cambio proporcionar cuando el comprador paga una compra en efectivo.
Escriba un programa que comience leyendo una cantidad de centavos del usuario como un entero. Luego, su programa debe calcular y mostrar las denominaciones de las monedas que se deben usar para dar esa cantidad de cambio al comprador. Los cambios deben darse usando la menor cantidad de monedas posible. Suponga que la máquina está cargada con monedas de un centavo, cinco centavos, diez centavos, cuartos, loonies y toonies.
Una moneda de un dólar se introdujo en Canadá en 1987. Se conoce como a loonie porque una cara de la moneda tiene un bribón (un tipo de pájaro). La moneda de dos dólares, conocida como toonie, se introdujo 9 años después. Su nombre se deriva de la combinación del número dos y el nombre del loonie.

[Ejercicio 13](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio13.py)

## Ejercicio 14
Muchas personas piensan en su altura en pies y pulgadas, incluso en algunos países que utilizan principalmente el sistema métrico. Escriba un programa que lea un número de pies del usuario, seguido de un número de pulgadas. Una vez que se leen estos valores, su programa.

[Ejercicio 14](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio14.py)

## Ejercicio 15
En este ejercicio, creará un programa que comienza leyendo una medida en pies del usuario. Luego, su programa debe mostrar la distancia equivalente en pulgadas, yardas y millas. Use Internet para buscar los factores de conversión necesarios si no los tiene memorizados.

[Ejercicio 15](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio15.py)

## Ejercicio 16
Escriba un programa que comience leyendo un radio, r, del usuario. El programa continuará calculando y mostrando el área de un círculo con radio r y el volumen de una esfera con radio r. Use la constante pi en el módulo matemático en sus cálculos.
Sugerencia: El área de un círculo se calcula usando el área de fórmula = π*r^2. El volumen de una esfera se calcula usando la fórmula volumen = 4/3 * π* r^3.

[Ejercicio 16](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio16.py)

## Ejercicio 17
La cantidad de energía requerida para aumentar la temperatura de un gramo de un material en un grado Celsius es la capacidad de calor específica del material, C. La cantidad total de energía requerida para elevar m gramos de un material en ΔT grados Celsius se puede calcular usando la fórmula:
q = mCΔT.
Escriba un programa que lea la masa de un poco de agua y el cambio de temperatura del usuario. Su programa debe mostrar la cantidad total de energía que debe agregarse o eliminarse para lograr el cambio de temperatura deseado.
Sugerencia: La capacidad calorífica específica del agua es 4.186 J g◦C. Debido a que el agua tiene una densidad de 1.0 gramo por mililitro, puede usar gramos y mililitros de manera intercambiable en este ejercicio.

[Ejercicio 17](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio17.py)

## Ejercicio 18 
El volumen de un cilindro se puede calcular multiplicando el área de su base circular por su altura. Escriba un programa que lea el radio del cilindro, junto con su altura, del usuario y calcule su volumen. Muestra el resultado redondeado a un decimal.

[Ejercicio 18](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio18.py)

## Ejercicio 19
Escriba un programa que determine como un objeto viaja cuando golpea el piso. El usuario insertara la información de la altura desde donde el objeto se deja caer, en metros(m) dado que el objeto se deja caer desde el reposo (Velocidad inicial V0= 0 m/s). Asumiendo que la aceleración debido a la gravedad es 9.81 m/s^2 y usando la formula Vf= raiz (Vo ^2 + 2gd). 
Calcule la velocidad final Vf usando la velocidad inicial V0 
La aceleración = g, la distancia = d

[Ejercicio 19](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio19.py)

## Ejercicio 20
La ley de los gases ideales es una aproximación matemática del comportamiento de los gases a medida que cambian la presión, el volumen y la temperatura. Por lo general, se indica como:
PV = nRT
donde P es la presión en Pascales, V es el volumen en litros, n es la cantidad de sustancia en moles, R es la constante de gas ideal, igual a 8.314 J mol K, y T es la temperatura en grados Kelvin.
Escriba un programa que calcule la cantidad de gas en moles cuando el usuario suministra la presión, el volumen y la temperatura. Pruebe su programa determinando la cantidad de moles de gas en un tanque de buceo. Un tanque típico de SCUBA contiene 12 litros de gas a una presión de 20,000,000 Pascales (aproximadamente 3,000 PSI). La temperatura ambiente es de aproximadamente 20 grados Celsius o 68 grados Fahrenheit.
Sugerencia: una temperatura se convierte de Celsius a Kelvin al agregarle 273.15. Para convertir una temperatura de Fahrenheit a Kelvin, deduzca 32 de ella, multiplíquela por 5/9 y luego agregue 273.15.

[Ejercicio 20](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio20.py)

## Ejercicio 21
El área de un triángulo se puede calcular usando la siguiente fórmula, donde b es la longitud de la base del triángulo y h es su altura:
área = b × h / 2
Escriba un programa que permita al usuario ingresar valores para b y h. Luego, el programa debe calcular y mostrar el área de un triángulo con longitud base b y altura h.

[Ejercicio 21](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio21.py)

## Ejercicio 22
En el ejercicio anterior, se creó un programa que calculaba el área de un triángulo cuando se conocía la longitud de su base y su altura. También es posible calcular el área de un triángulo cuando se conocen las longitudes de los tres lados. Sean s1, s2 y s3 las longitudes de los lados. Sea s = (s1 + s2 + s3) / 2. Entonces el área del triángulo
se puede calcular usando la siguiente fórmula:
área = s × (s - s1) × (s - s2) × (s - s3)
Desarrolle un programa que lea las longitudes de los lados de un triángulo del usuario y muestre su área.

[Ejercicio 22](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio22.py)

## Ejercicio 23
Un polígono es regular si sus lados tienen la misma longitud y los ángulos entre todos los lados adyacentes son iguales. El área de un polígono regular se puede calcular usando la siguiente fórmula, donde s es la longitud de un lado y n es el número de lados:
área = (n × s^2) / (4 × tan (π/ n))
Escriba un programa que lea s y n del usuario y luego muestre el área de un polígono regular construido a partir de estos valores

[Ejercicio 23](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio23.py)

## Ejercicio 24
Crear un programa que le pida al usurario la duracion en dias. horas. minutos y segundos. Calcular y desplegar la cantidad total de segundos de duracion 

[Ejercicio 24](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio24.py)

## Ejercicio 25
En este ejercicio usted revertira el proceso descrito en el ejercicio previo.Desarrolle un programa que comnienze por leer una cantidad en segundos introducidos por el usuario. Su programa debe desplegar la cantidad equivlente en forma de D:HH:NN:SS, Donde D son los dias, HH las horas, MM los minutos y SS los segundos.las horas, minutos y segundos deben estar en formato de 2 digitos, con un 0 al inicio, si es necesario.

[Ejercicio 25](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio25.py)

## Ejercicio 26
Python incluye una biblioteca de funciones para trabajar con el tiempo, incluida una función llamada “asctime” en el módulo de “tiempo”. Lee la hora actual del reloj interno de la computadora y la devuelve en un formato legible para humanos. Escriba un programa que muestre la hora y fecha actuales. Su programa no requerirá ninguna entrada del usuario.

[Ejercicio 26](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio26.py)

## Ejercicio 27
Escriba un programa que calcule el índice de masa corporal (IMC) de un individuo. Su programa debe comenzar leyendo una altura y un peso del usuario. Utilizando la siguiente formula:
IMC = masa/peso^2

[Ejercicio 27](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio27.py)

## Ejercicio 28
Cuando el viento sopla en clima frío, el aire se siente aún más frío de lo que realmente es porque el movimiento del aire aumenta la velocidad de enfriamiento de los objetos cálidos, como las personas. Este efecto se conoce como sensación térmica.
En 2001, Canadá, el Reino Unido y los Estados Unidos adoptaron la siguiente fórmula para calcular el índice de sensación térmica. Dentro de la fórmula “Ta” está la temperatura del aire en grados Celsius y “V” es la velocidad del viento en kilómetros por hora.
Se puede usar una fórmula similar con diferentes valores constantes con temperaturas en grados Fahrenheit y velocidades del viento en millas por hora.
WCI = 13.12 + 0.6215Ta − 11.37V0.16 + 0.3965TaV0.16
Escriba un programa que comience leyendo la temperatura del aire y la velocidad del viento del usuario. Una vez que se hayan leído estos valores, su programa debería mostrar el índice de enfriamiento del viento redondeado al entero más cercano.
El índice de enfriamiento del viento solo se considera válido para temperaturas inferiores o iguales a 10 grados Celsius y velocidades del viento superiores a 4,8 kilómetros por hora

[Ejercicio 28](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio28.py)

## Ejercicio 29
Escriba un programa que comience leyendo una temperatura del usuario en grados Celsius. Luego, su programa debe mostrar la temperatura equivalente en grados Fahrenheit y grados Kelvin. Los cálculos necesarios para convertir entre diferentes unidades de temperatura se pueden encontrar en Internet.

[Ejercicio 29](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio29.py)

## Ejercicio 30
En este ejercicio creará un programa que lee la presión del usuario en kilopascales. Una vez que se haya leído la presión, su programa debe informar la presión equivalente en libras por pulgada cuadrada, milímetros de mercurio y atmósferas. Usa tus habilidades de investigación para determinar los factores de conversión entre estas unidades

[Ejercicio 30](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio30.py)

## Ejercicio 31
Desarrolle un programa que lea un número entero de cuatro dígitos del usuario y muestre la suma de los dígitos en el número. Por ejemplo, si el usuario ingresa 3141, entonces su programa debería mostrar 3 + 1 + 4 + 1 = 9.

[Ejercicio 31](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio31.py)

## Ejercicio 32
Cree un programa que lea tres enteros del usuario y los muestre en orden, ordenado (de menor a mayor). Use las funciones min y max para encontrar los valores más pequeños y más grandes. El valor medio se puede encontrar calculando la suma de los tres valores y luego restando el valor mínimo y el valor máximo.

[Ejercicio 32](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio32.py)

## Ejercicio 33
Una panadería vende hogazas de pan por $ 3.49 cada una. El pan de un día tiene un descuento del 60 por ciento. Escriba un programa que comience leyendo la cantidad de hogazas de pan de un día compradas al usuario. Luego, su programa debe mostrar el precio regular del pan, el descuento porque tiene un día de antigüedad y el precio total. Todos los valores deben mostrarse usando dos decimales, y los puntos decimales en todos los números deben alinearse cuando el usuario ingresa valores razonables.

[Ejercicio 33](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio33.py)

# Control de flujo 
Si un programa no fuera más que una lista de órdenes a ejecutar de forma secuencia una por una no tendría mucha utilidad.
La sentencia condicional nos permite comprobar condiciones y hacer que nuestro programa se comporte de una forma u otra que ejecute un fragmento de código u otro dependiente de otra condición.
Aquí es donde cobran su importancia el tipo booleano y los operadores lógicos e irracionales.

# Condicional IF
La forma más simple de una sentencia condicional es un “ if “ (del inglés “si”). Seguido de la condición a evaluar, dos puntos (:) e identado el código a ejecutar en caso de que se cumpla dicha condición.

## Ejemplo
Password == input(‘inserta el pasword: ’)

If password == ‘Comunitesh’:

        Print (‘password correcto’)

La identacion del código se realiza con cuatro espacios.

# Condición if….. else

Esta estructura permite añadir un comportamiento en caso de que la condicion no resulte cierta.

## Ejemplo:
Else:

Print(‘te equivocaste’)

# Estructura if… elif…elif…else
El comando elif es la contracción de else..if , en español “ si no”

## Ejemplo:

Edad = in(input(‘inserta tu edad: ‘))

If  edad > 60:

    Print(‘Eres un adulto mayor’) 


## Ejercicio 34
Escriba un programa que lea un numero entero por el usuario.
Su programa debe despleglar un mensaje indicando si su numero entero es par o impar

[Ejercicio 34](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio34.py)

## Ejercicio 35
Se dice comúnmente que un año humano es equivalente a 7 años de perro. Sin embargo, esta simple conversión no reconoce que los perros alcanzan la edad adulta en aproximadamente dos años. Como resultado, algunas personas creen que es mejor contar cada uno de los primeros dos años humanos como 10.5 años de perro, y luego contar cada año humano adicional como 4 años de perro.
Escriba un programa que implemente la conversión de años humanos a años de perros descritos en el párrafo anterior. Asegúrese de que su programa funcione correctamente para conversiones de menos de dos años humanos y para conversiones de dos o más años humanos. Su programa debe mostrar un mensaje de error apropiado si el usuario ingresa un número negativo.

[Ejercicio 35](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio35.py)

## Ejercicio 36
En este ejercicio creará un programa que lee una letra del alfabeto del usuario. Si el usuario ingresa a, e, i, o, u, entonces su programa debe mostrar un mensaje que indica que la letra ingresada es una vocal. Si el usuario ingresa Y entonces su programa debería mostrar un mensaje que indica que a veces Y es una vocal, y a veces Y es una consonante. De lo contrario, su programa debería mostrar un mensaje indicando que la letra es una consonante.

[Ejercicio 36](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio36.py)

## Ejercicio 37 
Escriba un programa que determine el nombre de una forma a partir de su número de lados. Lea el número de lados del usuario y luego informe el nombre apropiado como parte de un mensaje significativo. Su programa debe admitir formas con desde 3 hasta (e incluyendo) 10 lados. Si se ingresa un número de lados fuera de este rango, entonces su programa debería mostrar un mensaje de error apropiado.

[Ejercicio 37](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio37.py)

## Ejercicio 38
La duración de un mes varía de 28 a 31 días. En este ejercicio creará un programa que lee el nombre de un mes del usuario como una cadena. Luego, su programa debería mostrar la cantidad de días en ese mes. Muestre “28 o 29 días” para febrero para que se aborden los años bisiestos.

[Ejercicio 38](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio38.py)

## Ejercicio 39
La siguiente tabla enumera el nivel de sonido en decibelios para varios ruidos comunes.

|RUIDO             |NIVEL DE DECIBELES (dB) |
|------------------|-----------------------:|
|Martillo naumatico|130                     |
|Cortador de cesped|106                     |
|Despertador       |70                      |
|Cuarto tranquilo  |40                      |


Escriba un programa que lea un nivel de sonido en decibelios del usuario. Si el usuario ingresa un nivel de decibelios que coincide con uno de los ruidos en la tabla, entonces su programa debería mostrar un mensaje que contenga solo ese ruido. Si el usuario ingresa una cantidad de decibelios entre los ruidos enumerados, entonces su programa debe mostrar un mensaje que indique entre qué ruidos se encuentra el nivel. Asegúrese de que su programa también genere una salida razonable para un valor menor que el ruido más bajo de la tabla y para un valor mayor que el ruido más alto de la tabla.

[Ejercicio 39](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio39.py)

## Ejercicio 40
Un triángulo se puede clasificar en función de la longitud de sus lados como equilátero, isósceles o escaleno. Los 3 lados de un triángulo equilátero tienen la misma longitud. Un triángulo isósceles tiene dos lados que tienen la misma longitud y un tercer lado que tiene una longitud diferente. Si todos los lados tienen diferentes longitudes, entonces el triángulo es escaleno. Escriba un programa que lea las longitudes de 3 lados de un triángulo del usuario. Muestra un mensaje que indica el tipo de triángulo.

[Ejercicio 40](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio40.py)

## Ejercicio 41
La siguiente tabla enumera una octava de notas musicales, comenzando con C central, junto con sus frecuencias.

|NOTA             |FRECUENCIA (Hz) |
|-------------------|--------------------------:|
|C4       |261.63                           |
|D4       |293.66                           |
|E4        |329.63                          |
|F4        |349.23                          |
|G4       |392.00                          |
|A4       |440.00                           |
|B4       |493.88                           |

Comience escribiendo un programa que lea el nombre de una nota del usuario y muestre la frecuencia de la nota. Su programa debe admitir todas las notas enumeradas anteriormente.
Una vez que tenga su programa funcionando correctamente para las notas enumeradas anteriormente, debe agregar soporte para todas las notas de C0 a C8. Si bien esto podría hacerse agregando muchos casos adicionales a su declaración if, dicha solución es engorrosa, poco elegante e inaceptable para los propósitos de este ejercicio. En cambio, debe explotar la relación entre las notas en octavas adyacentes. En particular, la frecuencia de cualquier nota en octava “n” es la mitad de la frecuencia de la nota correspondiente en octava n + 1. Al usar esta relación, debería poder agregar soporte para las notas adicionales sin agregar casos adicionales a su declaración if.

[Ejercicio 41](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio41.py)

## Ejercicio 42
En la pregunta anterior, convertiste del nombre de la nota a la frecuencia. En esta pregunta escribirás un programa que revierte ese proceso. Comience leyendo una frecuencia del usuario. Si la frecuencia está dentro de un Hertz de un valor que figura en la tabla de la pregunta anterior, informe el nombre de la nota. De lo contrario, informe que la frecuencia no corresponde a una nota conocida. En este ejercicio solo necesita considerar las notas enumeradas en la tabla. No hay necesidad de considerar notas de otras octavas.

[Ejercicio 42](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio42.py)

## Ejercicio 43
Es común que las imágenes de los líderes anteriores de un país, u otras personas de importancia histórica, aparezcan en su dinero. Las personas que aparecen en los billetes en los Estados Unidos son las siguientes.
Escriba un programa que comience leyendo la denominación de un billete del usuario. Luego, su programa debe mostrar el nombre de la persona que aparece en el billete de la cantidad ingresada. Se debe mostrar un mensaje de error apropiado si no existe dicha cantidad.

|NOMBRE             |CANTIDAD |
|-------------------|--------------------------:|
|George Washington       |$1                         |
|Thomas Jefferson|$2                           |
|Abraham Lincoln|$5                          |
|Alexander Hamilton|$10                          |
|Andrew Jackson|$20                          |
|Ulysses S. Grant|$50                           |
|Benjamin Franklin|$100                           |

[Ejercicio 43](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio43.py)

## Ejercicio 44
Canadá tiene días tres feriados nacionales que caen en las mismas fechas cada año. Escriba un programa que lea un mes y un día del usuario. Si el mes y el día coinciden con uno de los feriados enumerados anteriormente, entonces su programa debería mostrar el nombre del feriado. De lo contrario, su programa debería indicar que el mes y el día ingresados no corresponden a un día festivo de fecha fija.
Canadá tiene dos feriados nacionales adicionales, el Viernes Santo y el Día del Trabajo, cuyas fechas varían de un año a otro. También hay numerosas fiestas provinciales y territoriales, algunas de las cuales tienen fechas fijas y otras tienen fechas variables. No consideraremos ninguno de estos días festivos adicionales en este ejercicio.

|CELEBRACIÓN             |FECHA |
|-------------------|--------------------------:|
|Año nuevo      | Enero 1                     |
|Dia de Canada| julio 1                          |
|Navidad| Diciembre 25                          |

[Ejercicio 44](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio44.py)

## Ejercicio 45
Las posiciones en un tablero de ajedrez se identifican con una letra y un número. La letra identifica la columna, mientras que el número identifica la fila, como se muestra a continuación:

Escriba un programa que lea una posición del usuario. Use una declaración if para determinar si la columna comienza con un cuadrado negro o un cuadrado blanco. Luego use la aritmética modular para informar el color del cuadrado en esa fila. Por ejemplo, si el usuario ingresa a1, su programa debe informar que el cuadrado es negro. Si el usuario ingresa d5, entonces su programa debe informar que el cuadrado es blanco. Su programa puede asumir que siempre se ingresará una posición válida. No necesita realizar ninguna comprobación de errores.

[Ejercicio 45](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio45.py)

## Ejercicio 46
El año esta dividido en cuatro temporadas: Primavera, verano, otoño e invierno. Aunque las fechas exacatas cambian un poco dependiendo del año, usemos las siguientes fechas:

|TEMPORADA             |PRIMER DIA |
|-------------------|--------------------------:|
|Primavera      | Marzo 21                   |
|Verano | Junio 21                          |
|Otoño | Septimebre 22                          |
|Invierno | Diciembre 21                          |

Escriba un programa en el que el usuario introduzca el mes y dia.
El usuario introducira el nombre del mes como una 'string' seguido del dia como entero 'int'
Su programa debe desplegar la temporada de acuerdo a la informacion introducida por el usuario.

[Ejercicio 46](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio46.py)

## Ejercicio 47
Los horóscopos comúnmente reportados en los periódicos usan la posición del sol en el momento del nacimiento para intentar predecir el futuro. Este sistema de astrología divide el año en doce signos del zodiaco, como se describe en la tabla a continuación:

|Signo zodiacal | Fechas |
|Capricornio |Diciembre 22 to Enero 19| 
|Aquario |Enero 20 to Febrero 18| 
|Piscis |Febrero 19 to Marzo 20| 
|Aries |Marzo 21 to Abril 19| 
|Tauro |Abril 20 to Mayo 20| 
|Geminis |Mayo 21 to Junio 20| 
|Cancer |Junio 21 to Julio 22| 
|Leo |Julio 23 to Agosto 22| 
|Virgo |Agosto 23 to Septiembre 22| 
|Libra |Septiembre 23 to Octubre 22| 
|Escorpion |Octubre 23 to Noviembre 21| 
|Sagitario |Noviembre 22 to Diciembre 21|

Escriba un programa que le pida al usuario que ingrese su mes y día de nacimiento. Luego, nuestro programa debe informar el signo zodiacal del usuario como parte de un mensaje de salida apropiado.

[Ejercicio 47](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio47.py)

## Ejercicio 48
El zodiaco chino asigna animales a años en un ciclo de 12 años. Un ciclo de 12 años se muestra en la tabla a continuación. El patrón se repite a partir de ahí, con 2012 siendo otro año del dragón, y 1999 siendo otro año de la liebre.

|Año |Animal| 
|----------|----------|
|2000 |Dragón| 
|2001 |Serpiente |
|2002 |Caballo |
|2003 |Oveja|
|2004 |Mono| 
|2005 |Gallo |
|2006 |Perro |
|2007 |Cerdo |
|2008 |Rata |
|2009 |Buey |
|2010 |Tigre| 
|2011| Liebre|

Escriba un programa que lea un año del usuario y muestre el animal asociado con ese año. Su programa debería funcionar correctamente durante cualquier año mayor o igual a cero, no solo los que figuran en la tabla.

[Ejercicio 48](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio48.py)

## Ejercicio 49
La siguiente tabla contiene rangos de magnitud de terremotos en la escala de Richter y sus descriptores:

|Magnitud| Tipos|
|---------|-----------| 
|Menor que 2.0| Micro| 
|2.0 Menor que 3.0| Muy suave| 
|3.0 Menor que 4.0| Suave |
|4.0 Menor que 5.0 |Ligero|
|5.0 Menor que 6.0 |Moderado| 
|6.0 Menor que 7.0 |Fuerte| 
|7.0 Menor que 8.0 |Mayor|
|8.0 Menor que 10.0| Grande| 
|10.0 o más |Meteórico|

Escriba un programa que lea una magnitud del usuario y muestre el descriptor apropiado como parte de un mensaje significativo. Por ejemplo, si el usuario ingresa 5.5, entonces su programa debe indicar que un terremoto de magnitud 5.5 se considera un terremoto moderado.

[Ejercicio 49](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio49.py)










