Excelente!

:interrobang: Mas por que `LinearRegression` retorna um vetor de coeficientes em vez de apenas o declive? E por que devemos tratar os valores de `X` de maneira diferente dos de `y`? Na verdade, por que estamos chamando `X` com letras maiúsculas agora?

:bulb: É que `LinearRegression` também funciona para realizar regressões lineares múltiplas, nas quais ao invés de inserir uma única variável e obter um único coeficiente (o declive), nos permitirá trabalhar com um **vetor** de variáveis (` X`, sim, maiúscula)...

<pre>
<código>X = (x<sub>1</sub>, x<sub>2</sub>,..., x<sub>n</sub>)</code>
</pre>

...e obtenha um vetor de coeficientes (`coef_`)...

<pre>
<code>coef_ = (β<sub>1</sub>, β <sub>2</sub>, ,..., β<sub>n</sub></code>
</pre>

...com o qual formará a expressão linear:

<pre>
<code>y = f (X) = β<sub>0</sub> + β<sub>1</sub> × x<sub>1</sub>, β<sub>2</sub> × x<sub> 2</sub>,..., β<sub>n</sub> × x<sub>n</sub></code>
</pre>

Mas como estamos trabalhando com regressões lineares simples, temos um único ** ** `x` (sim, letras minúsculas) torna as coisas mais... simples :stuck_out_tongue_closed_eyes::

<pre>
<code>y = f(x) = β<sub>0</sub> + β <sub>1</sub> × x</code>
</pre>
