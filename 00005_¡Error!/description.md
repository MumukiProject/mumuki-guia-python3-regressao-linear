Embora quando fazemos _regressão linear simples_ começamos com a suposição de que todos os nossos dados caem em uma reta que descreve a relação entre nossas variáveis ​​`x` e `y` :sunglasses: ...

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-regresion-lineal/master/assets/lineal_ideal_1672261074446.png" alt="lineal_ideal_1672261074446.png" width="auto" height="auto">

...as observações _muito_ raramente (bah, nunca :rindo:) eles vão cumprir essa idealidade. Em vez disso, nossos dados ficarão assim :disappointed::

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-regresion-lineal/master/assets/lineal_noisy_1672261280083.png" alt="lineal_noisy_1672261280083.png" width="auto" height="auto">


Como cada valor se desvia da _reta ideal_ por um valor de erro aleatório (`ε`), a equação geral para um modelo de regressão linear simples será a seguinte:

<pre>
<code>f(x) = b + m × x + ε</code>
</pre>

Agora, se sobrepormos este modelo e os dados reais...

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-regresion-lineal/master/assets/lineal_error_1672261651436.png" alt="lineal_error_1672261651436.png" width="auto" height="auto">

... poderíamos tentar calcular **a distância** entre o valor real de cada `y` observado e seu valor ideal. Por esse motivo, também é comum ver a equação expressa em termos vetoriais, relacionando os valores que `x` e `y` assumem como uma série de observações `i`, onde para cada uma delas vale o seguinte:  

<pre>
<code>y<sub>i</sub> = β<sub>0</sub> + β<sub>1</sub> × x<sub>i</sub> + ε<sub>i</sub></code>
</pre>

Da mesma forma, <code>β<sub>0</sub></code> corresponde à ordenada da origem (ou seja, o valor de y quando todas as outras variáveis são zero), <code>β<sub>1</sub></code> com o efeito médio da mudança em `x` em `y` e <code>ε<sub>i</sub></code> com **a distância** entre nossa linha ideal e cada observação.

> Mas não se desespere! O fato de os valores ideais e observados não coincidirem perfeitamente não nos impedirá de procurar (e eventualmente estabelecer) uma relação entre `x` e `y` :muscle:. Junte-se a nós no seguinte exercício para entender como fazê-lo!
