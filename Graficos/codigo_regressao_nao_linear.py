# importando pacotes e módulos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score
import scipy.stats as stats

dataset = pd.read_csv('Dados_Experimentais - Página1.csv')
sns.scatterplot(data=dataset, x='circunferência', y='superfície', hue='circunferência')

plt.title('Circunferência vs Superfície')
plt.xlabel('Circunferência')
plt.ylabel('Superfície')
plt.show()

# ajuste polinomial de grau 2 ou ajuste quadrático
model = np.poly1d(np.polyfit(dataset['circunferência'], dataset['superfície'], 2))

# Visualização de linha polinomial
polyline = np.linspace(0, 321, 100)
plt.scatter(dataset['circunferência'], dataset['superfície'])
plt.plot(polyline, model(polyline))
plt.xlabel('Circunferência')
plt.ylabel('Superfície')
plt.show()

print(model)

# r métrica quadrada
print(r2_score(dataset['superfície'], model(dataset['circunferência'])))
