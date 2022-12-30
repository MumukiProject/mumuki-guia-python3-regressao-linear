Ya podemos decir que hemos ajustado nuestro modelo, caracterizado y evaluado. De esta forma, no sólo podemos explicar la relación entre las variables, sino que también podemos determinar su poder predictivo y compararlo con el de otros modelos más sofisticados que eventualmente realicemos. ¡Lo logramos! 🥲

Peeeeeero, aún no hicimos aquello a lo que vinimos, ¿verdad? ¡Intentemos predecir valores! :tada: Primero, definamos una función para hacer más sencillo el uso del `modelo`:

```python
def predecir_respuesta(imc):
  return modelo.predict([[imc]])[0]
```

Y ahora probemos con un índice de masa corporal ["normal" según la OMS](https://es.wikipedia.org/wiki/%C3%8Dndice_de_masa_corporal): 

```python
ム predecir_respuesta(20)
1881.9868473136542
```

¿Qué, qué? ¡Esto no puede estar bien! El máximo valor de `response` es de aproximadamente 350:

```python
max(diabetes["response"])
346.0
```

🤦 ¿Qué pasó entonces? Si volvemos a la descripción de este lote de datos que nos proveyó inicialmente `scikit-learn`, veremos que dice lo siguiente: 

_(...) each of these 10 feature variables have been mean centered and scaled (...)_ (_cada una de estas 10 variables han sido centradas y escaladas_)

¡Allí está el problema! El valor del índice de masa corporal fue transformado. Pero a no desesperar, que podemos revertir la transformación así: 

```python
def transformar_imc(imc):
  # los valores originales del IMC se encuentran acá 
  # https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt
  # No desarrollaremos el proceso para obtener estos coeficientes, pero 
  # te invitamos a que lo deduzcas usando lo que vimos en esta lección 🤭
  return (imc - 26.375791855203694) / 92.78055277 

def predecir_respuesta(imc):
  return modelo.predict([[transformar_imc(imc)]])[0]
```

Ahora los resultados tienen más sentido :clap:: 

```python
ム predecir_respuesta(20)
85.05642088787117
ム predecir_respuesta(30)
190.17295167042818
```

> Ahora te toca a vos: escribí otra versión de la función `predecir_respuesta`, pero que esta vez no utilice el `modelo` del último ejercicio sino sus valores de <code>β<sub>0</sub></code> y <code>β<sub>1</sub></code>. 
> 

