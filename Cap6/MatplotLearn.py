import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Tracando graficos
x = np.array([1, 2, 3, 4, 5])
y = x*2
y2 = x*x
plt.plot(x, y, label='y = x*2', color='red', marker='o', linestyle='dashed', linewidth=2, markersize=12)
plt.plot(x, y2, label='y = x*x', color='blue', marker='s', linewidth=2, markersize=12)
plt.show()

# Usando subplots
plt.subplot(1, 2, 1)
plt.plot(x, y, label='y = x*2', color='red', marker='o', linestyle='dashed', linewidth=2, markersize=12)
plt.subplot(1, 2, 2)
plt.plot(x, y2, label='y = x*x', color='blue', marker='s', linewidth=2, markersize=12)
plt.show()

# Usando dataframes do pandas com matplotlib
df = pd.read_csv('paises.csv', delimiter=';', encoding='utf-8')
maisRicos = df.nlargest(7, 'GDP ($ per capita)')
plt.scatter(maisRicos['Country'], maisRicos['GDP ($ per capita)'], maisRicos['Area (sq. mi.)']/1000)
plt.legend()
plt.show()
