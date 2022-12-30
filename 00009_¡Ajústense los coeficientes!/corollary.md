¡Excelente!

:interrobang: Pero, ¿por qué `LinearRegression` nos devuelve un vector de coeficientes en lugar de sólamente la pendiente? ¿Y por qué debemos tratar a los valores de `X` de forma diferente a los de `y`? De hecho, ¿por qué ahora estamos llamando a `X` con mayúsculas?

:bulb: Es que `LinearRegression` funciona también para realizar regresiones lineales múltiples, en las que en lugar de ingresar una única variable y obtener un único coeficiente (la pendiente), nos permitirá trabajar con un **vector** de variables (`X`, sí, en mayúsculas)...

<pre>
<code>X = (x<sub>1</sub>, x<sub>2</sub>,..., x<sub>n</sub>)</code>
</pre>

...y obtener un vector de coeficientes (`coef_`)...

<pre>
<code>coef_ = (β<sub>1</sub>, β<sub>2</sub>, ,..., β<sub>n</sub></code>
</pre>

...con el que conformará la expresión lineal:

<pre>
<code>y = f(X) = β<sub>0</sub> + β<sub>1</sub> × x<sub>1</sub>, β<sub>2</sub> × x<sub>2</sub>, ,..., β<sub>n</sub> × x<sub>n</sub></code>
</pre>

Pero como estamos trabajando con regresiones lineales simples, tenemos una **única** `x` (sí, en minúsculas) las cosas nos quedan más... simples :stuck_out_tongue_closed_eyes::

<pre>
<code>y = f(x) = β<sub>0</sub> + β<sub>1</sub> × x</code>
</pre>
