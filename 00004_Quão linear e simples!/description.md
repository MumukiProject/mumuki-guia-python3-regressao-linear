A primeira técnica de aprendizado automático  que veremos nos permitirá realizar regressões: _estudar_ e _prever_ as colunas de um conjunto de dados. 🔢 Em palavras um pouco mais formais, tentaremos encontrar uma fórmula...

<pre>
<code>y = f(x<sub>1</sub>, x<sub>2</sub>, .. ., x <sub>n</sub>)</code>
</pre>

...onde os `y` e `x`s representam variáveis ​​aleatórias: `y` é aquela que tentaremos prever, e o vetor <code>X = (x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>)</code> o conjunto que tentará explicá-lo. Alguns exemplos:

* 🏘 A partir de um lote de dados domiciliares com colunas `preço`, `idade`, `área`, poderíamos tentar explicar o `preço` (variável `y`) com base nos outras duas variáveis (​​<code>x<sub>1</sub></code> e <code>x<sub>2</sub></code>)
* 🌊 A partir de um lote de dados de medição oceanográfica, poderíamos tentar estabelecer uma ligação entre ` temperatura` e `salinidade` da água do mar, e prever a primeira (`y`) em função da última (`x`) (ou vice-versa, dependendo do contexto).

Neste estudo, vamos nos concentrar em um tipo de relacionamento: **linear**. Este método estatístico é usado para descrever uma variável contínua como uma função de uma ou várias variáveis ​​independentes, ajustando uma equação linear.

> Vamos tirar o pó (se estiverem debaixo do pó, claro 🤧) dos nossos conhecimentos matemáticos! Se tentássemos usar regressão linear para prever `y` como uma função de uma única variável, qual deveria ser a forma de nosso `f(x)`? 🤔
