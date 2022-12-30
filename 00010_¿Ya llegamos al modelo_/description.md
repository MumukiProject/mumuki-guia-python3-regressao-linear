¿Terminamos? Sí y no :person_shrugging:. Sí, por un lado pudimos establecer que existe un vínculo entre ambas variables (`corr ≈ 0.6`) y que dicho vínculo no parece el mero producto del azar (`pvalue ≪ 0.05`), y por otro pudimos aproximarlo a una recta, Pero aún estamos lejos de haber evaluado completamente al modelo. 🙃 

❓ ¡Es que aún hay muchas cosas que no sabemos! Por ejemplo: ¿cuán bueno es el modelo? ¿Los datos caen efectivamente en la recta? ¿Cuánto se alejan de ella? 

Una primera aproximación a las dos primeras preguntas es utilizar la métrica <code>R<sup>2</sup></code>, que nos indica cuán bueno es el ajuste del modelo.Esta medida estadística oscila entre `0` (los datos predicho no se ajustan a las observaciones) y `1` (los datos predichos se ajustan perfectamente a las observaciones). 

La operación `score` de nuestro `modelo` nos retornará justamente esta métrica (que dicho sea de paso, en los modelos de regresión lineal **simple** su valor se corresponde con el cuadrado de la correlación de Pearson 💡): 
 
```python
print("Coeficiente de determinación R²:", modelo.score(X.values, y)) 
```

> Obtené <code>R<sup>2</sup></code> y en base a este resultado, respondé: ¿cuán bueno resultó el modelo?
