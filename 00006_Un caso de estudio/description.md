Para continuar aprendiendo qué es y cómo se implementa un modelo de **regresión lineal simple**, utilizaremos un lote de datos bien conocido y usado en la literatura, [_Diabetes_](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html), que mide cuantitativamente el grado de avance a lo largo de un año de la enfermedad en 442 pacientes. Para ello, vamos a primero importar algunas bibliotecas, además de nuestra ya bien conocida `pandas`:
 
  * 🔢 `scipy`: una biblioteca de algoritmos matemáticos, muy útiles en el campo de la ciencia de datos; 
  * 📈 `seaborn`, `matplotlib`: herramientas de graficación que complementan y extienden a las operaciones `.plot` provistas por `pandas`;
  * 🤖 `sklearn` (abreviatura de _scikit-learn_): una popular biblioteca con algoritmos de aprendizaje automático, entre los cuales se encuentra, obviamente, soporte para regresión lineal 🎊 

```python
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import pearsonr, spearmanr
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# configuraciones opcionales para hacer a nuestros 
# gráficos más "bonitos"
plt.rcParams['image.cmap'] = "bwr"
plt.rcParams['savefig.bbox'] = "tight"
plt.style.use('ggplot')
```

Luego, procederemos a cargar el lote de datos que nos interesa. En este caso, lo obtendremos de la propia biblioteca `scikit-learn`, que lo trae de regalo 🎁 entre sus datos de ejemplo...

```python
from sklearn import datasets

diabetes = datasets.load_diabetes(as_frame=True)
print(diabetes['DESCR']) 
```

... y realizaremos algunos ajustes a su estructura para que sea un poco más _tratable_: 

```python
diabetes = pd.concat((diabetes['data'], diabetes['target']), axis='columns')
diabetes = diabetes.rename(columns={
    'bmi':'body_mass_index',
    'bp':'average blood pressure',
    's1':'total_serum_cholesterol',
    's2':'low_density_lipoproteins',
    's3':'high_density_lipoproteins',
    's4':'total_cholesterol',
    's6':'blood_sugar_level',
    'target': 'response'})
del diabetes['s5']

diabetes
```

> :woman_construction_worker::man_construction_worker: Manos a la obra: copiá y ejecutá **todo** el código anterior en un nuevo cuaderno. Luego seleccioná cuáles de las siguientes afirmaciones son válidas. 
