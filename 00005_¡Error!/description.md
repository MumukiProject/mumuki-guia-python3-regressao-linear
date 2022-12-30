Si bien cuando realizamos una _regresión lineal simple_ partimos de la suposición de que todos nuestros datos caen sobre una recta que describe la relación entre nuestras variables `x` e `y` :sunglasses: ...

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-regresion-lineal/master/assets/lineal_ideal_1672261074446.png" alt="lineal_ideal_1672261074446.png" width="auto" height="auto">

...las observaciones _muy_ rara vez (bah, nunca :laughing:) cumplirán con esta idealidad. Mas bien, nuestros datos se verán así :disappointed::

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-regresion-lineal/master/assets/lineal_noisy_1672261280083.png" alt="lineal_noisy_1672261280083.png" width="auto" height="auto">


Como cada valor se aparta de la _recta ideal_ en un valor aleatorio de error (`ε`), es que la ecuación general correspondiente a un modelo de regresión lineal simple será más bien la siguiente:

<pre>
<code>f(x) = b + m × x + ε</code>
</pre>

Ahora, si superponemos este modelo y los datos reales...

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-regresion-lineal/master/assets/lineal_error_1672261651436.png" alt="lineal_error_1672261651436.png" width="auto" height="auto">

... podríamos intentar calcular **la distancia** entre el valor real de cada `y` observado y su valor ideal. Por eso, la ecuación es frecuente también verla expresada en términos vectoriales, relacionando los valores que `x` e `y` toman como una serie de `i` observaciones, donde para cada una ellas se cumple que:  

<pre>
<code>y<sub>i</sub> = β<sub>0</sub> + β<sub>1</sub> × x<sub>i</sub> + ε<sub>i</sub></code>
</pre>

Análogamente, <code>β<sub>0</sub></code> se corresponde con la ordenada al origen (es decir, el valor de `y` cuando las demás variables son cero), <code>β<sub>1</sub></code> con el efecto promedio que tiene el cambio en `x` sobre `y` y <code>ε<sub>i</sub></code> con **la distancia** entre nuestra recta ideal y cada observación.

> ¡Pero a no desesperar! Que los valores ideales y observados no coincidan perfectamente no nos impedirá buscar (y eventualmente, establecer) una relación entre `x` e `y` :muscle:. ¡Acompañános al siguiente ejercicio para entender cómo hacerlo!

