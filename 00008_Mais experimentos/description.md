Tudo parece indicar que existe uma ligação entre o índice de massa corporal e a progressão do diabetes nos pacientes deste lote de dados. Com isso em mente, podemos agora tentar expressar esta  relação como `response = f(body_mass_index)`, onde `f` é uma função linear, certo? 😀

Bem, embora tenhamos elementos para explorar essa possibilidade, não vamos nos apressar 🐢. A relação pode ainda não ser **linear**, ou pode nem ser _significativa_ e simplesmente casual. :confused:

Portanto, antes de continuar faremos mais alguns testes. 📈 Primeiro, traçaremos as observações usando um `regplot`, que combina um gráfico de dispersão e sobrepõe os resultados em uma linha de regressão ideal:

```python
# Scatterplot + regressão, realizado com
seaborn sns.regplot(x="body_mass_index", y="response", data=diabetes)
```

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guide-python3-linear-regression/master/assets/diabetes_with_regression_1672268060049.png " alt ="diabetes_with_regression_1672268060049.png" width="auto" height="auto">

Bom 👍! Podemos ver que a linha ideal parece acompanhar as observações. 🧮 Façamos então nosso segundo teste, que consiste em calcular o _coeficiente de correlação de Pearson_ e seu _P-valor_ (ou em inglês, _P-value_):

  1. O primeiro é, novamente, uma medida de co-variação entre as variáveis, tal que valores absolutos próximos a `1` indicam alta correlação, enquanto aqueles próximos a `0` indicam baixa correlação;
  2. A segunda é uma medida de confiança que nos dirá quão _provável_ é que os resultados sejam produto do acaso. Quanto mais próximo de zero, menos provável é que o resultado seja um produto do acaso e, na prática, qualquer valor acima de `0.05` (ou `0.01`, se mais rigor for procurado) geralmente é considerado não significativo.

```python
# Coeficiente de correlação de Pearson e seu valor P
corr, pvalue = pearsonr(
  x = diabetes['body_mass_index'],
  y = diabetes['response'])
print("Coeficiente de correlação de Pearson:", corr )
print(" P-value:", pvalue)
```

> Execute este novo teste e compare-o com a correlação calculada anteriormente com `corr()`. Que conclusões você pode tirar?
