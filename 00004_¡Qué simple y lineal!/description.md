<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Math&display=swap" rel="stylesheet">

La primera técnica de aprendizaje automático que veremos nos permitirá realizar regresiones: _estudiar_ y _predecir_ las columnas de un conjunto de datos.  🔢 En palabras un poco más formales, intentaremos encontrar una fórmula...

<pre>
<code>y = f(x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>)</code>
</pre>

...donde la `y` y las `x`s representan variables aleatorias: `y` es aquella que intentaremos predecir, y el vector <code>X = (x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>)</code> el conjunto que intentará explicarla. Algunos ejemplos: 

* 🏘 A partir de un lote de datos de hogares con columnas `precio`, `antigüedad`, `superficie`, podríamos intentar explicar el `precio` (variable `y`) en función de las otras dos (variables <code>x<sub>1</sub></code> y <code>x<sub>2</sub></code>)
* 🌊 A partir de un lote de datos de mediciones oceanográficas, podríamos intentar establecer un vínculo entre `temperatura` y `salinidad` del agua marina, y predecir la primera (`y`) en función de la segunda (`x`) (o al revés, dependiendo del contexto).

Dentro de este estudio nos enfocaremos en un tipo de relación:  **lineal**. Este método estadístico se usa para describir una variable continua como una función de una o varias variables independientes, mediante el ajuste de una ecuación, justamente, lineal.

> ¡Desempolvemos (si es que están bajo polvo, claro 🤧) nuestros conocimientos matemáticos! Si tratáramos de emplear regresión lineal para predecir `y` en función de una única variable, ¿cuál debería ser la forma de nuestra `f(x)`? :thinking:
