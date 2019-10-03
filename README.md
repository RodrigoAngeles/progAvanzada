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

# Ejercicio 19
Escriba un programa que determine como un objeto viaja cuando golpea el piso. El usuario insertara la información de la altura desde donde el objeto se deja caer, en metros(m) dado que el objeto se deja caer desde el reposo (Velocidad inicial V0= 0 m/s). Asumiendo que la aceleración debido a la gravedad es 9.81 m/s^2 y usando la formula Vf= raiz (Vo ^2 + 2gd). 
Calcule la velocidad final Vf usando la velocidad inicial V0 
La aceleración = g, la distancia = d

[Ejercicio 19](https://github.com/RodrigoAngeles/progAvanzada/blob/master/ejercicio19.py)




