Todo parece indicar que existe un vínculo entre el índice de masa corporal y el avance de la diabetes en los pacientes de este lote de datos. Con esto en mente, ya podemos intentar expresar este vínculo como `response = f(body_mass_index)`, siendo `f` una función lineal, ¿no? 😀

Bueno, si bien tenemos elementos para explorar esa posibilidad, no nos apresuremos 🐢. La relación podría aún no ser **lineal**, o incluso podría no ser _significativa_ y deberse a, lisa y llanamente, la casualidad. :confused: 

Por eso, antes de continuar haremos algunas pruebas más. 📈 Primero, graficaremos las observaciones empleando un `regplot`, que combina un gráfico de dispersión y superpone los resultados sobre una recta ideal de regresión: 

```python
# Gráfico de dispersión + regresión, realizado con seaborn
sns.regplot(x="body_mass_index", y="response", data=diabetes)
```

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-regresion-lineal/master/assets/diabetes_with_regression_1672268060049.png" alt="diabetes_with_regression_1672268060049.png" width="auto" height="auto">

¡Bien 👍! Podemos ver que la recta ideal parece acompañar a las observaciones. 🧮 Realicemos entonces nuestra segunda prueba, consistente en calcular el _coeficiente de correlación de Pearson_ y su _valor P_ (o en inglés, _P-value_): 

  1. El primero es nuevamente, una medida de co-variación entre las variables, tal que valores absolutos cercanos a `1` indican alta correlación, mientras que los cercanos a `0` indican correlación baja;
  2. El segundo es una medida de confianza que nos dirá cuán _probable_ es que los resultados sean producto de la casualidad. Cuanto más cercana a cero, menos probable es que el resultado sea producto del azar y en la práctica se suele tomar cualquier valor por encima de `0.05` (o `0.01`, si se busca más rigor) como no significativo.

```python
# Coeficiente de correlación de Pearson y su valor P
corr, pvalue = pearsonr(
  x = diabetes['body_mass_index'], 
  y = diabetes['response'])
print("Coeficiente de correlación de Pearson:", corr) 
print("P-value:", pvalue) 
```

> Ejecutá esta nueva prueba y comparala con la correlación que calculaste anteriormente con `corr()`. ¿Qué conclusiones podés sacar?
