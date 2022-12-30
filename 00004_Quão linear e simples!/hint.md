Se nenhuma dessas equações lhe disser nada, você também pode tentar representá-las dando alguns valores arbitrários para `m` e `b`:

```python
import pandas as pd
import seaborn as sns

# Geramos algum x, de 0.1 a 4.9
df = pd .DataFrame({"x": map(lambda x: x/10, range(1, 50))})

# Geramos y para diferentes f(x)'s
# fazendo b = arbitrariamente 10 e m = 2
df["b × m + x"] = df["x"].map(lambda x: 10 * 2 + x)
df["b + m × x"] = df["x"].map(lambda x: 10 + 2 * x)
df["x² + x"] = df["x"].map(lambda x: x**x + x)
df["(m / x) + b"] = df["x"].map(lambda x: 5 / x + 12)
df

# Traçamos cada uma das curvas anteriores
# ⚠️ É importante plotar cada uma delas em uma célula diferente do seu cuaderno
sns.lineplot(dados=df, x= "x", y="b × m + x")
sns.lineplot(dados=df, x="x", y="b + m × x")
sns.lineplot(data=df, x="x)", y="x² + x")
sns.lineplot(data=df, x="x", y="(m / x) + b")
```

Qual ou quais delas representam **retas**? :straight_ruler:
