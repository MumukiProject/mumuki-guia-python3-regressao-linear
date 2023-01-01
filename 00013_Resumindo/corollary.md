Braaaavo! Já temos nosso primeiro modelo de regressão linear simples funcionando. Se você tentar com vários valores ou desenhar a linha reta obtida...

```python
# gráfico semelhante ao que fizemos anteriormente usando regplot
# mas agora usando as previsões do modelo que ajustamos
sns.scatterplot(x="body_mass_index", y="response", data=diabetes)
sns.lineplot(x="body_mass_index", y=modelo.predict(X = X.values), data=diabetes)
```

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guide-python3-linear-regression/master/assets/regplot_real_1672436347390.png" alt="regplot_real_1672436347390.png" width="auto" height=" carro">

... você vai perceber que muitos dos resultados não coincidem ao esperado, porque afinal ainda é a nossa primeira aproximação.

🧑‍🌾 _Não é muito, mas é trabalho honesto._
