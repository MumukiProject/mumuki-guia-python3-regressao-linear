La tabla anterior puede resultar abrumadora al principio :sweat:. Dado que sólo nos interesa analizar el vínculo con una variable en particular (en este caso, `response`, dado que será nuestra `y` que intentaremos predecir) podemos analizar sólo las correlaciones con dicha variable:

```python
correlaciones['response']
```

Por otro lado, para cada variable la matriz de correlación incluye en su diagonal la correlación entre ella y sí misma, que siempre será `1` y no nos aporta información.
