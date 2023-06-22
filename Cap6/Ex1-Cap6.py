import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfpaises = pd.read_csv('paises.csv', delimiter=';', encoding='utf-8')
dfspace = pd.read_csv('space.csv', delimiter=';', encoding='utf-8')

print(dfpaises.head())
print(dfspace.head())

# 1 Grafico de barras com quantas empresas são dos Estados Unidos e da China
print('1 Grafico de barras com quantas empresas são dos Estados Unidos e da China')
usa = dfspace[dfspace['Location'].str.contains('USA')]['Company Name'].unique()
china = dfspace[dfspace['Location'].str.contains('China')]['Company Name'].unique()
print(len(usa))
print(len(china))
plt.bar(['USA', 'China'], [len(usa), len(china)])
plt.show()

# 2 Dois graficos de linha no mesmo plano mostrando a mortalidade e a natalidade dos paises da America do Norte
print('2 Dois graficos de linha no mesmo plano mostrando a mortalidade e a natalidade dos paises da America do Norte')
americaNorte = dfpaises[dfpaises['Region'].str.contains('NORTHERN AMERICA')]
plt.plot(americaNorte['Country'], americaNorte['Birthrate'], label='Natalidade')
plt.plot(americaNorte['Country'], americaNorte['Deathrate'], label='Mortalidade')
plt.legend()
plt.show()
