# Biblioteca
import matplotlib.pyplot as plt
import numpy as np

## Parâmetros onde x é circunferência, x1 é circunferência ao quadrado e y superfície.
x = [60, 140, 172, 213, 287]
x1 = [3600, 19600, 29584, 45369, 82369]
y = [350, 1625, 2300, 3750, 6475]

## Gráfico da circunferência e superfície
plt.scatter(x,y)
plt.xlabel('Circunferência')
plt.ylabel('Superfície')
plt.title('Gráfico da circunferência')
plt.show()

## Gráfico da circunferência ao quadrado e superfície

plt.scatter(x1,y)
plt.xlabel('Circunferência ao quadrado')
plt.ylabel('Superfície')
plt.title('Gráfico da circunferência ao quadrado')
plt.show()
## plt.savefig('local/grafico.png')
