🥱 Embora possamos interpretar os valores RMSE levando em consideração a unidade `y`, não seria mais conveniente ajustar este valor para que seja expresso em um maneira adimensional? É assim que a métrica _RMSE normalizado_ surge:

<pre>
<code>RMSE<sub>normalizado</sub> = RMSE / (y<sub>max</sub> - y<sub>min</sub>)</code>
</pre>

Desta forma podemos obter valores entre `0` e `1`, onde os valores mais próximos de `0` representam modelos de melhor ajuste.

> Agora é a sua vez: calcule o valor RMSE<sub>normalizado</sub> do modelo obtido no exercício anterior.
