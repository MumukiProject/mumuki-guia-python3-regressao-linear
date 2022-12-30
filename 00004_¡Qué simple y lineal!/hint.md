Si ninguna de estas ecuaciones te dice nada, podés también probar graficarlas dándole algunos valores arbitrarios a `m` y `b`:

```python
import pandas as pd
import seaborn as sns

# Generamos algunos x, del 0.1 al 4.9
df = pd.DataFrame({"x": map(lambda x: x/10, range(1, 50))})

# Generamos y para diferentes f(x)'s
# haciendo, arbitrariamente, b = 10 y m = 2
df["b × m + x"] = df["x"].map(lambda x: 10 * 2 + x)
df["b + m × x"] = df["x"].map(lambda x: 10 + 2 * x)
df["x² + x"] = df["x"].map(lambda x: x**x + x)
df["(m / x) + b"] = df["x"].map(lambda x: 5 / x + 12)
df

# Graficamos cada una de las curvas anteriores
# ⚠️ Es importante graficar cada una de ellas en una celda diferente de tu cuaderno
sns.lineplot(data=df, x="x", y="b × m + x")
sns.lineplot(data=df, x="x", y="b + m × x")
sns.lineplot(data=df, x="x", y="x² + x")
sns.lineplot(data=df, x="x", y="(m / x) + b")
```

¿Cuál o cuáles de ellas representan **rectas**? :straight_ruler:
