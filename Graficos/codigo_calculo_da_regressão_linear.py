# Biblioteca
import matplotlib.pyplot as plt
import numpy as np
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
