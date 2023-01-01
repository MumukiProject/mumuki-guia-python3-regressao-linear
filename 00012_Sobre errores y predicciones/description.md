Como mencionamos anteriormente, o método mais utilizado para o ajuste do modelo linear é o dos mínimos quadrados ordinários (_OLS_), que identifica como melhor modelo a reta (ou plano se for regressão múltipla) que minimiza a soma dos quadrados dos erros...

<pre>
<code>ε<sup>2</sup> = ∑ (yi - ŷi)<sup>2</sup></code>
</pre >

...onde <code>y<sub>i</sub></code> são os valores observados e <code>ŷ<sub>i</sub></code> os valores estimados.

Mas essa fórmula tem dupla utilidade, pois podemos partir dela para gerar outro parâmetro da bondade do modelo 😇: a raiz do erro quadrático médio (_RMSE_, por sua sigla em inglês). O RMSE mede apenas a raiz quadrada do erro (<code>∑ (yi - ŷi)<sup>2</sup></code>), em média. Novamente `scikit-learn` nos fornece uma função `mean_squared_error` para nos ajudar com este cálculo:

```python
y_pred = modelo.predict(X = X_test)

rmse = mean_squared_error(
  y_true = y_test,
  y_pred = y_pred,
  squared = False
)

print("RMSE:", rmse)
```
> Agora é sua vez: gere uma nova partição `train / test` de `75% / 25%` e `random_state = 42` e liste os parâmetros obtidos. 
