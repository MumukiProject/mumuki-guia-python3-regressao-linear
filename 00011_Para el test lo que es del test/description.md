🔮 Ao trabalhar com modelos preditivos, não é apenas importante ajustá-los, mas também quantificar sua capacidade de prever novas observações.
 
Para realizar esta avaliação, vamos treiná-lo novamente, mas aplicando uma metodologia muito comum na área de aprendizado automático: separar os dados em dois conjuntos de dados, um para treinamento (`train`) e outro para teste (`test` ). Vamos resolver isso com a ajuda da função `scikit-learn` `train_test_split`, que particionará nossas `X` e `y`, cada uma, em dois conjuntos:
 
```python
X = diabetes[['body_mass_index'] ]
y = diabetes['response']
 
X_train, X_test, y_train, y_test = train_test_split(
  X.values.reshape(-1,1),
  y.values,
  train_size = 0,8,
  random_state = 42,  
  shuffle = True
)
```                               	 
 
Então, usaremos o par `(X_train, y_train)` para ajustar os coeficientes de nosso regressor...
 
```python
model = LinearRegression()
modelo.fit(X = X_train, y = y_train)
print("Intercepto :", modelo.intercept_)
print("Declive:", list(zip(X.columns, modelo.coef_.flatten())))
```
 
...mas agora vamos testar a capacidade preditiva usando o par `(X_test, y_test)` :
 
```python
print("Coeficiente de determinação R²:", modelo.score(X_test.values, y_test))
```
 
Dessa forma, evitamos _trapacear_ e avaliar o modelo usando os próprios dados os quais foi treinado 😉.
 
> Vamos ver se entendeu: treine o modelo novamente, mas seguindo essa metodologia. Tente fazer isso várias vezes, com diferentes valores `random_state`, ou sem especificar nenhum valor (para que `train_test_split` sempre retorne diferentes divisões aleatórias)
>
> Você vê agora alguma mudança nos coeficientes e em <code>R<sup>2</sup></code>?
