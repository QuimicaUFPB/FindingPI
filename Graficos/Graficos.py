# Biblioteca
import matplotlib.pyplot as plt
import numpy as np

## Parâmetros onde x é circunferência, x1 é circunferência ao quadrado e y superfície.
x = [60, 140, 172, 213, 287, 25, 95, 124, 212, 285, 321]
x1 = [3600, 19600, 29584, 45369, 82369, 625, 9025, 15376, 44944, 81225, 103041]
y = [350, 1625, 2300, 3750, 6475, 50.0, 656.9, 1114.4, 3225.0, 6243.8, 7625.0]

## Gráfico da circunferência e superfície
plt.scatter(x,y)
plt.xlabel('Circunferência')
plt.ylabel('Superfície')
plt.grid()
plt.savefig('/content/sample_data/grafico_circunferencia.png')

## Gráfico da circunferência ao quadrado e superfície

plt.scatter(x1,y)
plt.xlabel('Circunferência ao quadrado')
plt.ylabel('Superfície')
plt.grid()
plt.savefig('/content/sample_data/grafico_circunferencia_quadrado.png')

## calculo de regressão linear

param=np.polyfit(x1,y,1) # ajuda a curva
print('parâmetros: ',param) #mostra os parâmetros
a, b = param
print('reta: y = %.5f * x + %.5f' % (a, b))
#gráfico da regressão linear
x_fit=np.linspace(-0.1,103041.1,1000)
y_fit=np.polyval(param,x_fit)
plt.plot(x1,y,'r.',label='Dados Originais')
plt.plot(x_fit,y_fit,'b--',label='Curva Ajustada')
plt.xlabel('Circunferência ao quadrado')
plt.ylabel('Superfície')
plt.legend()
plt.savefig('/content/sample_data/grafico_regressao_linear.png')
