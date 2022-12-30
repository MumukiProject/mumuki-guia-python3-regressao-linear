Como mencionamos anteriormente, el método más utilizado para el ajuste del modelo lineal es el de mínimos cuadrados ordinarios (_OLS_), que identifica como mejor modelo la recta (o plano si es regresión múltiple) que minimiza la suma de los cuadrados de los errores...

<pre>
<code>ε<sup>2</sup> = ∑ (yi - ŷi)<sup>2</sup></code>
</pre>

...donde <code>y<sub>i</sub></code> son los valores observados e <code>ŷ<sub>i</sub></code>, los valores estimados. 

Pero esta fórmula tiene una doble utilidad, porque podemos partir de ella para generar otro parámetro de la bondad del modelo 😇: la raíz del error cuadrático medio (_RMSE_, por sus siglas en inglés). RMSE mide justamente la raíz cuadrada del error (<code>∑ (yi - ŷi)<sup>2</sup></code>), promediado. Nuevamente `scikit-learn` nos provee una función `mean_squared_error` para asistirnos con este cálculo:

```python
y_pred = modelo.predict(X = X_test)

rmse = mean_squared_error(
  y_true  = y_test,
  y_pred  = y_pred,
  squared = False
)

print("RMSE:", rmse)
```

> Ahora te toca a vos: generá una nueva partición `train / test` de `75% / 25%` y `random_state = 42` y detallá los parámetros obtenidos.  