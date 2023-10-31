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
## plt.savefig('FindingPI/Graficos/grafico_circunferencia.png')

## Gráfico da circunferência ao quadrado e superfície

plt.scatter(x1,y)
plt.xlabel('Circunferência ao quadrado')
plt.ylabel('Superfície')
plt.title('Gráfico da circunferência ao quadrado')
plt.show()
## plt.savefig('FindingPI/Graficos/grafico_circunferencia_quadrado.png')

## calculo de regressão não linear

param=np.polyfit(x1,y,1) # ajuda a curva
print('parâmetros: ',param) #mostra os parâmetros
a, b = param
print('reta: y = %.5f * x + %.5f' % (a, b))
#gráfico
x_fit=np.linspace(-0.1,82369.1,1000)
y_fit=np.polyval(param,x_fit)
plt.plot(xs,ys,'r.',label='Dados Originais')
plt.plot(x_fit,y_fit,'b--',label='Curva Ajustada')
plt.xlabel('Circunferência ao quadrado')
plt.ylabel('Superfície')
plt.legend()
