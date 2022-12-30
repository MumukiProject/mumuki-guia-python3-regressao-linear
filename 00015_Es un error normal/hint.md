Como punto de partida, podés usar la siguiente función: 

```python
def normalizar_rmse(rmse, y):
  return rmse / (max(y) - min(y))
```
