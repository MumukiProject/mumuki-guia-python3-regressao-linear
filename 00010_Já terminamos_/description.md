Terminamos? Sim e não :person_shrugging:. Sim, por um lado conseguimos constatar que existe uma ligação entre ambas as variáveis ​​(`corr ≈ 0,6`) e que essa ligação não parece ser mero produto do acaso (`pvalor ≪ 0,05`), e por o outro conseguimos aproximá-lo a uma reta, mas ainda estamos longe de ter avaliado o modelo completamente. 🙃

❓É que ainda existem muitas coisas que não sabemos! Por exemplo: quão bom é o modelo? Os dados realmente estão na reta? A que distância dela?

Uma primeira aproximação para as duas primeiras questões é usar a métrica <code>R<sup>2</sup></code>, que nos diz quão bom é o ajuste do modelo. Essa medida estatística oscila entre `0` (os dados previstos não se ajustam às observações) e `1` (os dados previstos se ajustam perfeitamente às observações).

A operação `score` do nosso `modelo` retornará justamente esta métrica (que, aliás, em modelos de regressão linear **simples** seu valor corresponde ao quadrado da correlação de Pearson 💡):
 
```python
print("Coeficiente de determinação R²:", modelo.score(X.values, y))
```

> Obtenha <code>R<sup>2</sup></code> e com base neste resultado, responda: quão bom é o modelo?
