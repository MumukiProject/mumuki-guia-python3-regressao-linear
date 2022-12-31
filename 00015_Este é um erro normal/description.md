🥱 Si bien podemos interpretar los valores de RMSE teniendo en cuenta la unidad de `y`, ¿no resultaría más cómodo ajustar este valor para que quede expresado de forma adimensional? Así es como surge la métrica _RMSE normalizado_:

<pre>
<code>RMSE<sub>normalizado</sub> = RMSE / (y<sub>max</sub> - y<sub>min</sub>)</code>
</pre>

De este modo podremos obtener valores entre `0` y `1`, donde los valores más cercanos a `0` representan modelos de mejor ajuste.

> Ahora te toca a vos: calculá el valor de RMSE<sub>normalizado</sub> del modelo obtenido en el ejercicio anterior. 

