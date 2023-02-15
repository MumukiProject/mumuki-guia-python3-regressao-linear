Excelente! :confetti_ball: 


```python
ムcorrelaciones['response']
age                          0.187889
sex                          0.043062
body_mass_index              0.586450 # <= esta é a correlação que nos interessa
average blood pressure       0.441484
total_serum_cholesterol      0.212022
low_density_lipoproteins     0.174054
high_density_lipoproteins   -0.394789
total_cholesterol            0.430453
blood_sugar_level            0.382483
response                     1.000000
```

Se confiarmos exclusivamente na correlação, _parece_ que pessoas com maior [índice de massa corporal](https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal) têm maior desenvolvimento da doença. Podemos afirmar isso porque:

  * Em termos absolutos, a correlação entre essas duas variáveis é maior que `0.5` (lembre-se que `0` representa nenhuma correlação e `1`, a correlação máxima);
  * E também a correlação tem sinal positivo, o que indica uma relação direta.

Outra forma útil de visualizar essas correlações é por meio de um [_mapa de calor_](https://pt.wikipedia.org/wiki/Mapa_de_calor) 🥵, que atribui pontos mais leves aos pares com maior correlação:

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-regresion-lineal/master/assets/heatmap_1672264640360.png" alt="heatmap_1672264640360.png" width="auto" height="auto">

(:eyes: _olhe a terceira coluna da última linha, ou o que é o mesmo, na terceira linha da última coluna_)

Para gerá-la, você pode fazer o seguinte:

```python
sns.heatmap(correlaciones.abs())
```

:wave: Experimente e até o próximo exercício.
 

  