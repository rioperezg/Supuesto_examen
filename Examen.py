""""
Ejercicio 1
El trabajo que realizaremos consiste en la elaboración de un modelo para resolver sudokus, para ello, crea una función que resuelva 
un Sudoku de 9x9.
Un sudoku es un puzzle matemático que se construye sobre una rejilla de 9x9 casillas. El objetivo es rellenarla con números 
enteros del 1 al 9 según las siguientes restricciones:
No se pueden repetir números en una misma fila.
No se pueden repetir números en una misma columna.
No se pueden repetir números en una misma subcuadrícula de 3x3 de las 9 que componen la rejilla.
Esta función recibe un argumento que consiste en una matriz de 2D. Un valor de 0 representa un cuadrado desconocido.
El sudoku a resolver ha de estar bien planteado, i.e., ha de tener solución única. Esto se cumple si se parte de unas condiciones 
iniciales adecuadas, que consisten en números ya fijados en algunas de las casillas del sudoku. Un sudoku bien planteado sin resolver 
podría ser, e.g., el mostrado en la siguiente figura:


Ejercicio 2
Cree una función expand que tome una expresión con una sola variable de una letra y la expanda. La fórmula tiene la forma (ax b)^n. 
donde a y b son números enteros positivos o negativos, x es cualquier variable de un solo carácter y n es un número natural.
Si a = 1, no se antepone ningún coeficiente a la variable.
Si a = -1, la variable tiene el prefijo "-".
La forma expandida debe devolverse como una cadena de la forma ax^b cx^d ex^f... donde a, c y e son los coeficientes del término y x 
es la variable original de una letra pasada.
La fórmula original y b, d y f son potencias de x en cada término, en orden descendente. Si el coeficiente de un término es cero, ese 
término no debe incluirse. Si un término tiene un coeficiente de 1, no incluya ese coeficiente.
Si un término tiene un coeficiente de -1, debe contener solo "-".
Si el término tiene una potencia de 0, solo se debe incluir el coeficiente. Si el término tiene una potencia de 1, el signo de 
intercalación y la potencia deben excluirse.
Ejemplos:
expand("(x+1)^2")      # returns "x^2+2x+1"
expand("(p-1)^3")      # returns "p^3-3p^2+3p-1"
expand("(2f+4)^6")     # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
expand("(-2a-4)^0")    # returns "1"
expand("(-12t+43)^2")  # returns "144t^2-1032t+1849"
expand("(r+0)^203")    # returns "r^203"
expand("(-x-1)^2")     # returns "x^2+2x+1"


Ejercicio 3
Es posible que muchos de ustedes ya estén familiarizados con los teléfonos inteligentes que emplean patrones geométricos como medida 
de seguridad. Para desbloquear el dispositivo, debe conectar una serie de puntos en una cuadrícula moviendo el dedo sin levantarlo 
mientras arrastra el patrón en la pantalla.
La siguiente imagen tiene siete ejemplos de patrón de punto/punto: (A -> B -> I -> E -> D -> G -> C).
Para este tipo, debe implementar una función que devuelva el número de patrones posibles a partir del punto inicial especificado y 
con la longitud especificada entre 4 y 9 puntos/puntos. 
Tenga en cuenta que este kata requiere devolver el número de patrones, no los patrones en sí , por lo que solo necesita contarlos. 
Además, el nombre de la función puede ser diferente según el lenguaje de programación utilizado, pero la idea sigue siendo la misma.
Normas
En un patrón, los puntos/puntos no se pueden repetir: solo se pueden usar una vez, como máximo.
En un patrón, dos puntos/puntos posteriores cualesquiera solo se pueden conectar con líneas rectas directas de cualquiera de estas 
formas:
Horizontalmente: como (A -> B) en la imagen del patrón de ejemplo.
Verticalmente: como (D -> G) en la imagen del patrón de ejemplo.
En diagonal: como (I -> E), así como (B -> I), en la imagen del patrón de ejemplo.
Pasando por encima de un punto entre ellos que ya ha sido 'usado': como (G -> C) pasando por encima de E, en la imagen del patrón de 
ejemplo. Esta es la regla más complicada. Normalmente, no podría conectar G con C, porque E está entre ellos, sin embargo , cuando E 
ya se ha utilizado como parte del patrón que está rastreando, puede conectar G con C pasando por E , porque E se ignora , como ya se 
usó una vez.


Ejercicio 4
Corre el año 1214. Una noche, el Papa Inocencio III se despierta y encuentra al arcángel Gabriel flotando ante él. Gabriel truena al 
Papa:
Reúne a todos los sabios de Pisa, especialmente a Leonardo Fibonacci. Para que las cruzadas en las Tierras Santas tengan éxito, estos 
hombres deben calcular el millonésimo número en la recurrencia de Fibonacci. Si no haces esto, tus ejércitos nunca recuperarán la 
tierra santa. es Su voluntad.
El ángel luego se desvanece en una explosión de luz blanca.
El Papa Inocencio III se sienta en su cama con asombro. ¿Cuánto es un millón? piensa para sí mismo. Nunca fue muy bueno en matemáticas.
Intenta escribir el número, pero debido a que todos en Europa todavía usan números romanos en este momento de la historia, no puede 
representar este número. Si tan solo supiera sobre la invención del cero, podría facilitar este tipo de cosas.
Decide volver a la cama. Se consuela, El Señor nunca me desafiaría así; esto debe haber sido algún engaño del diablo. Una pesadilla 
bastante horrenda, sin duda. Los ejércitos del Papa Inocencio III continuarían conquistando Constantinopla (ahora Estambul), pero nunca 
recuperarían la Tierra Santa como él deseaba....
Crea función que calcula el millonésimo número en la recurrencia de Fibonacci, sabiendo que debe usar un algoritmo iterativo para 
calcular el millonésimo número en la recurrencia de Fibonacci.Para ello ejecute los siguientes pasos
Primero, se inicializan los dos primeros números en la recurrencia (0 y 1).
Luego, se calculan los números sucesivos en la recurrencia usando la fórmula c = a + b, donde c es el número en la posición n, a es 
el número en la posición n - 1 y b es el número en la posición n - 2.
Este proceso se repite hasta llegar al millonésimo número en la recurrencia, que se devuelve como resultado.
Escriba un algoritmo que pueda manejar n hasta 2000000.
Su algoritmo debe generar la respuesta entera exacta, con total precisión. Además, debe manejar correctamente los números negativos 
como entrada.



ejercicio 5
El cifrado Rail Fence (también llamado cifrado en zigzag) es una forma de cifrado por transposición. Funciona escribiendo su mensaje 
en líneas alternas a lo largo de la página y luego leyendo cada línea por turno. Veamos el desglose paso a paso para cifrar un texto 
usando Rail Fence Cipher
Para encriptar un mensaje usando Rail Fence Cipher, primero necesitamos tener una clave (lo mismo para encriptar y desencriptar), que 
es el número de filas que tendrá para este cifrado.
Luego comenzamos a escribir las letras del texto sin formato dado en diagonal hacia el lado derecho hasta alcanzar el número de filas 
especificado por la clave.
Luego rebotamos hacia arriba de manera similar en diagonal hasta que llegamos a la primera fila nuevamente. Así, los alfabetos del 
texto plano se escriben en zig-zag.
Este ciclo continúa hasta que se alcanza el final del texto sin formato. Luego se leen las filas individuales para obtener el texto 
cifrado.
Considerar un ejemplo nos aclararía las cosas. Tomemos un ejemplo donde: El texto sin formato se da como " defend the east wall " y el 
número de rieles (clave) = 3, luego el proceso de encriptación es como se muestra a continuación:
El cifrado Rail Fence con una clave de 3
Tenga en cuenta que al final del mensaje hemos insertado dos letras "X", que se llaman nulos y actúan como marcadores de posición. 
Esto se hace para asegurarse de que el mensaje encaje perfectamente en la cuadrícula, de modo que haya el mismo número de letras en 
la fila superior y en la fila inferior.
Ahora, leer la imagen fila por fila nos da el texto cifrado como "DNETLEEDHESWLXFTAAX".
Para descifrar un texto cifrado codificado con Rail Fence Cipher, tenemos que reconstruir la cuadrícula diagonal utilizada para cifrar 
el mensaje. Comenzamos escribiendo el mensaje, pero dejando una estrella en lugar de los espacios por ocupar (como se muestra en la 
siguiente figura). Gradualmente, puede reemplazar todas las estrellas con las letras correspondientes y leer el texto sin formato de 
la tabla de manera similar al cifrado.
Colocación de estrellas en el lugar de los espacios a ocupar
Veamos el desglose por pasos:
Comenzamos haciendo una cuadrícula (matriz de rieles) con tantas filas como la clave dada (número de rieles) y tantas columnas como la 
longitud del texto cifrado.
Luego colocamos la primera letra en el cuadrado superior izquierdo y avanzamos en diagonal hacia abajo donde están presentes las letras.
Cuando volvemos a la fila superior, colocamos la siguiente letra en el texto cifrado. Continuamos este proceso a lo largo de la fila y 
comenzamos la siguiente fila cuando lleguemos al final.
Atravesamos la matriz en forma de zig-zag para obtener el texto plano original.
 Escriba una función/método que tome 2 argumentos, una cadena y el número de rieles, y devuelva la cadena CODIFICADA.
Escriba una segunda función/método que tome 2 argumentos, una cadena codificada y el número de rieles, y devuelva la cadena 
DECODIFICADA.
Tanto para la codificación como para la decodificación, asuma un número de rieles >= 2 y que pasar una cadena vacía devolverá una 
cadena vacía.
Tenga en cuenta que el ejemplo anterior excluye la puntuación y los espacios solo por simplicidad. Sin embargo, hay pruebas que 
incluyen puntuación. No filtre la puntuación, ya que son parte de la cadena.
Adjuntar archivoNinguno archivo selec.






"""
