De fato, o coeficiente de Person nos deu `0.58645...`, que coincide com o valor obtido por `corr()`. A razão é simples: `corr()` usa por padrão o método de Pearson (`'pearson'`)...

```python
# esta linha ...
diabates.corr()
# ... é equivalente a
diabates.corr('pearson')
```

...mas você pode usar outro método, como o coeficiente de correlação de Spearman (`'spearman'`):

```python
ム diabetes.corr('spearman')['response']
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

Da mesma forma, podemos usar a função `spearmanr` de `scipy`:

```python
ム spearmanr(diabetes['body_mass_index'], diabetes['response'])
SpearmanrResult(correlation=0.5613820101065616, pvalue=4.567023927725032e-38)
```

E por que existem vários métodos? É que cada um serve para situações diferentes! Especificamente, `pearsonr` destina-se a ser usado com variáveis que seguem uma [distribuição normal](https://pt.wikipedia.org/wiki/Distribui%C3%A7%C3%A3o_normal)...

<iframe width="560" height="315" src="https://www.youtube.com/embed/EvHiee7gs9Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

... considerando que `spearmanr` não tem esse requisito (que devemos primeiro testar realizando [um teste de normalidade como o de Shapiro-Wilk](https://pt.wikipedia.org/wiki/Teste_de_Shapiro%E2%80%93Wilk)), então a partir de agora usaremos o último.

