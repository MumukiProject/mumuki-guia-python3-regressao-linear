Antes de analisar as relações entre duas variáveis temos que... descobrir quais estão relacionadas! 😛

Embora não haja uma resposta exaustiva para essa pergunta, uma boa primeira maneira de abordá-la é gerar uma _matriz de correlação_, que nos dirá até que ponto as mudanças em qualquer uma das variáveis acompanham as mudanças em qualquer uma das outras ↔️. Para fazer isso, `DataFrame`s têm a operação `corr`:

```python
correlacoes = diabetes.corr()
correlacoes
```

Esta matriz mostrará, para cada par de variáveis, quão relacionadas elas estão em uma escala de ` - 1` a `1`, onde:

* `1`: altamente correlacionado é diretamente proporcional. ↗️ Se uma variável cresce, a outra também;
* `0`: sem nenhuma correlação. 🤷 Mudanças em um parecem não influenciar na outra;
* `-1`: altamente correlacionado e inversamente proporcional. ↘️ Se uma variável aumenta, a outra diminui.  

> É a sua vez: gere a matriz de correlação e marque quais afirmações na coluna `resposta` (um valor que indica o grau de progressão da doença para cada paciente) estão corretas.
