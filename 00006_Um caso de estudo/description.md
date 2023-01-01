Para continuar aprendendo o que é um modelo de **regressão linear simples** e como implementá-lo, usaremos um conjunto de dados bem conhecido e usado na literatura, [_Diabetes_](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html), que mediu quantitativamente o grau de progressão da doença ao longo de um ano em 442 pacientes. Para isso, vamos primeiro importar algumas bibliotecas, além dos nossos já conhecidos `pandas`:
 
  * 🔢 `scipy`: uma biblioteca de algoritmos matemáticos, muito útil na área de ciência de dados;
  * 📈 `seaborn`, `matplotlib`: ferramentas de graficação que complementam e estendem as operações `.plot` fornecidas pelos `pandas`;
  * 🤖 `sklearn` (abreviação de _scikit-learn_): uma biblioteca popular com algoritmos de aprendizado automático, obviamente incluindo suporte para regressão linear. 🎊


```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import pearsonr, spearmanr
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# configurações opcionais para tornar nossos
# gráficos mais bonitos
plt.rcParams['image.cmap'] = "bwr"
plt.rcParams['savefig.bbox'] = "tight"
plt.style.use('ggplot')
```

Em seguida, continuaremos a carregar o lote de dados em que estamos interessados. Neste caso, iremos obtê-lo da própria biblioteca `scikit-learn`, que o traz como brinde 🎁 entre seus dados de exemplo...

```python
from sklearn import datasets

diabetes = datasets.load_diabetes(as_frame=True)
print(diabetes['DESCR'])
```

... e faça alguns ajustes em sua estrutura para torná-la um pouco mais _tratável_:

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

> :woman_construction_worker::man_construction_worker: Mãos à obra: copie e execute **todo** o código acima em um novo cuaderno. Em seguida, selecione quais das seguintes declarações são válidas.
