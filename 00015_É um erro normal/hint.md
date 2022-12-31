Como ponto de partida, você pode usar a seguinte função:

```python
def normalizar_rmse(rmse, y):
  return rmse / (max(y) - min(y))
```
