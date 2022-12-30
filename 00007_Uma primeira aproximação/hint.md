A tabela acima pode ser esmagadora no início :sweat:. Como estamos interessados apenas em analisar o link para uma determinada variável (neste caso, `response`, já que será nosso `y` que tentaremos prever) podemos analisar apenas as correlações com essa variável:

```python
correlacoes['response']
```

Por outro lado, para cada variável a matriz de correlação inclui em sua diagonal a correlação entre ela e ela mesma, que sempre será `1` e não nos fornece nenhuma informação.
