En efecto, el coeficiente de Person nos arrojó `0.58645...`, que coincide con el valor obtenido mediante `corr()`. El motivo es simple: `corr()` utiliza por defecto el método de Pearson (`'pearson'`)...

```python
# esta línea ...
diabates.corr()
# ... es equivalente a 
diabates.corr('pearson')
```

Pero bien se podría usar otro método, como por ejemplo el coeficiente de correlación de Spearman (`'spearman'`): 

```python
ム diabetes.corr('spearman')['body_mass_index']['response']
age                          0.197822
sex                          0.037401
body_mass_index              0.561382
average blood pressure       0.416241
total_serum_cholesterol      0.232429
low_density_lipoproteins     0.195834
high_density_lipoproteins   -0.410022
total_cholesterol            0.448931
blood_sugar_level            0.350792
response                     1.000000
```

De igual forma, podemos usar la función `spearmanr` de `scipy`: 

```python
ム spearmanr(diabetes['body_mass_index'], diabetes['response'])
SpearmanrResult(correlation=0.5613820101065616, pvalue=4.567023927725032e-38)
```

¿Y por qué existen múltiples métodos? ¡Es que cada uno sirve para situaciones diferentes! Concretamente, `pearsonr` está pensado para ser usado con variables que siguen una [distribución normal](https://es.wikipedia.org/wiki/Distribuci%C3%B3n_normal)...

<iframe width="560" height="315" src="https://www.youtube.com/embed/EvHiee7gs9Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

... mientras que `spearmanr` no tiene esta exigencia  (la cual deberíamos primero evaluar realizando [una prueba de normalidad como el test de Shapiro-Wilk](https://es.wikipedia.org/wiki/Prueba_de_Shapiro%E2%80%93Wilk)), por lo que de ahora en más utilizaremos esta última. 







