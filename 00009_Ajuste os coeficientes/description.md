Agora que validamos gráfica e numericamente que a correlação é significativa (embora não muito forte, apenas ≈ `0,6`), podemos finalmente desenvolver (ou como costuma-se dizer, _ajustar_) nosso modelo de regressão linear simples. :raised_hands: Ajustar  
 
o modelo consiste em estimar, a partir dos dados disponíveis:
 
 - a linha que minimiza a distância `ε` entre as observações de `x` e esta
 - encontrar os valores dos coeficientes de regressão que maximizam a probabilidade de Deixe a linha prever os valores observados.
 
O método mais comumente usado para isso é o método dos mínimos quadrados (ou _OLS_) e é implementado por `scikit-learn` usando `LinearRegression()`:
 
```python
X = diabetes[['body_mass_index'] ]
y = diabetes['response']
 
modelo = LinearRegression()
modelo.fit(X = X.values, y = y)
```
 
Como vemos, devemos primeiro criar um `modelo` e depois ajustá-lo usando sua operação `fit` , indicando os valores de `X` e `y`. Então podemos imprimir os valores encontrados da ordenada para a origem (`intercept_`) e a declive (o primeiro valor do vetor `coef_`):
 
```python
print("Intercepto:", modelo.intercept_)
print("Declive:" , list(zip(X.columns, modelo.coef_.flatten())))
```
 
> Copie e execute o código acima e responda. Qual das equações **melhor representa** o modelo obtido?
