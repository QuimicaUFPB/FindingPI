# Biblioteca
import matplotlib.pyplot as plt
import numpy as np
## calculo de regressão linear

param=np.polyfit(x1,y,1) # ajuda a curva
print('parâmetros: ',param) #mostra os parâmetros
a, b = param
print('reta: y = %.5f * x + %.5f' % (a, b))
