Agora podemos dizer que ajustamos, caracterizamos e avaliamos nosso modelo. Desta forma, podemos não só explicar a relação entre as variáveis, como também determinar o seu poder preditivo e compará-lo com o de outros modelos mais sofisticados que venhamos a realizar. Fizemos! 🥲

Aiiiinda não fizemos o que viemos fazer aqui, certo? Vamos tentar prever valores! :tada: Primeiro, vamos definir uma função para facilitar o uso do `model`:

```python
def prever_resposta(imc):
  return modelo.predict([[imc]])[0]
```

E agora vamos tentar com um índice de massa corporal ["normal" segundo a OMS](https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal):

```python
ム antecipar_resposta(20)
1881.9868473136542
```

O que, o que? Isso não pode estar certo! O valor máximo de `resposta` é cerca de 350:

```python
max(diabetes["response"])
346.0
```

🤦 O que aconteceu então? Se voltarmos à descrição deste lote de dados que inicialmente nos foi fornecido pelo `scikit-learn`, veremos que diz o seguinte:

_(...) each of these 10 feature variables have been mean centered and scaled (...)_ _(cada uma dessas 10 variáveis de características foram centradas na média e dimensionadas)_

Ai que está o problema! O valor do índice de massa corporal foi transformado. Mas para não se desesperar, podemos reverter a transformação assim:

```python
def transformar_imc(imc):
   # valores originais de IMC podem ser encontrados aqui
   # https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt
   # Não desenvolveremos o processo para obter esses coeficientes, mas sim
   # convidamos você a deduzir usando o que vimos nesta lição 🤭
   retorno (imc - 26.375791855203694) / 92.78055277

def prever_resposta(imc):
   return model.predict([[transformar_imc(imc)]])[0]
```

Agora os resultados fazem mais sentido :clap::

```python
ム antecipar_resposta(20)
85.05642088787117
ム antecipar_resposta(30)
190.17295167042818
```

> Agora é a sua vez: eu escrevi outra versão da função `prever_resposta`, mas desta vez ela não usa o `model` do último exercício, mas seu <code>β<sub>0</sub></code > valores e <code>β<sub>1</sub></code>.
>

