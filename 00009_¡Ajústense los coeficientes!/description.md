Ahora que validamos gráfica y numéricamente que la correlación es significativa (aunque no muy fuerte, tan sólo ≈ `0.6`), podemos finalmente desarrollar (o como se suele decir frecuentemente, _ajustar_) nuestro modelo de regresión lineal simple. :raised_hands:  

💺 Ajustar al modelo consiste en estimar, a partir de los datos disponibles:

 - la recta que minimice la distancia `ε` entre las observaciones de `x` y ésta;
 - encontrar los valores de los coeficientes de regresión que maximizan la probabilidad de que la recta prediga los valores observados.

El método  más utilizado para ésto es el de mínimos cuadrados ordinarios (o _OLS_, por sus siglas en inglés) y `scikit-learn` lo implementa mediante `LinearRegression()`:

```python
X = diabetes[['body_mass_index']]
y = diabetes['response']

modelo = LinearRegression()
modelo.fit(X = X.values, y = y)
```

Como vemos, primero debemos crear un `modelo` y seguidamente ajustarlo utilizando su operación `fit`, indicando los valores de `X` e `y`.  Luego podremos imprimir los valores encontrados de ordenada al origen (`intercept_`) y la pendiente (el primer valor del vector `coef_`):

```python
print("Ordenada:", modelo.intercept_)
print("Pendiente:", list(zip(X.columns, modelo.coef_.flatten())))
```

> Copiá y ejecutá el código anterior y respondé. ¿Cuál de las ecuaciones **representa mejor** al modelo obtenido?