¡Braaaaavo! Ya tenemos nuestro primer modelo de regresión lineal simple funcionando. Si lo probás con múltiples valores o trazás la recta obtenida...

```python
# gráfica similar a que anteriormente realizamos usando regplot
# pero ahora utilizando a las predicciones del modelo que ajustamos
sns.scatterplot(x="body_mass_index", y="response", data=diabetes)
sns.lineplot(x="body_mass_index", y=modelo.predict(X = X.values), data=diabetes)
```

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-regresion-lineal/master/assets/regplot_real_1672436347390.png" alt="regplot_real_1672436347390.png" width="auto" height="auto">

... vas a notar que muchos de los resultados se apartan de lo esperado, porque al fin y al cabo no deja de ser nuestra primera aproximación. 

🧑‍🌾 _No será mucho, pero es trabajo honesto._ 

