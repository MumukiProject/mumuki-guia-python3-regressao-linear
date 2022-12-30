🔮 Al trabajar con modelos predictivos, no solo es importante ajustarlos, sino también cuantificar su capacidad para predecir nuevas observaciones.

Para poder hacer esta evaluación, vamos a volver a entrenarlo, pero aplicando una metodología  muy frecuente en el campo del aprendizaje automático: separar los datos en dos conjuntos de datos, uno de entrenamiento (`train`) y otro de prueba (`test`). Esto lo resolveremos con la ayuda de la función `train_test_split` de `scikit-learn`, que particionará nuestras `X` e `y`, cada una, en dos conjuntos: 

```python
X = diabetes[['body_mass_index']]
y = diabetes['response']

X_train, X_test, y_train, y_test = train_test_split(
  X.values.reshape(-1,1),
  y.values,
  train_size = 0.8,
  random_state = 42,  
  shuffle = True
)
```                                    

Luego, usaremos el par `(X_train, y_train)` para ajustar los coeficientes de nuestro regresor...

```python
modelo = LinearRegression()
modelo.fit(X = X_train, y = y_train)
print("Ordenada:", modelo.intercept_)
print("Pendiente:", list(zip(X.columns, modelo.coef_.flatten())))
```

...pero ahora evaluaremos la capacidad predictiva usando el par `(X_test, y_test)`:

```python
print("Coeficiente de determinación R²:", modelo.score(X_test, y_test))
```

De esta forma, evitaremos _hacer trampa_ y evaluar al modelo usando los propios datos con lo que fue entrenado 😉.

> Veamos si se va entendiendo: entrená nuevamente al modelo, pero siguiendo esta metodología. Probá hacerlo varias veces, con diferentes valores de `random_state`, o directamente sin especificar ningún valor (para que `train_test_split` arroje siempre divisiones al azar diferentes)
>
> ¿Ves ahora algún cambio en los coeficientes y en <code>R<sup>2</sup></code>?
