# Biblioteca
import matplotlib.pyplot as plt
import numpy as np

## Parâmetros onde x e circunferência ao quadrado e y superfície.
x = [3600, 19600, 29584, 45369, 82369]
y = [350, 1625, 2300, 3750, 6475]

## Gráfico da circunferência ao qquadrado e superfície

plt.scatter(x,y)
plt.xlabel('Circunferência ao quadrado')
plt.ylabel('Superfície')
plt.title('Gráfico da circunferência')
plt.show()
## plt.savefig('local/grafico.png')
