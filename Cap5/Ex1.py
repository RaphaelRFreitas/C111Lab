import pandas as pd
import numpy as np

df = pd.read_csv('paises.csv', delimiter=';', encoding='utf-8')
# 1.a Mostre os paises que sao da OCEANIA
print('1.a Mostre os paises que sao da OCEANIA')
print(df[df['Region'].str.contains('OCEANIA')])
# 1.b Mostre a quantidade de paises que sao da OCEANIA
print('1.b Mostre a quantidade de paises que sao da OCEANIA')
oceania = df[df['Region'].str.contains('OCEANIA')]
print(len(oceania))

# 2 Mostre a media de taxa de alfabetizacao de todos os paises
print('2 Mostre a media de taxa de alfabetizacao de todos os paises')
print(df['Literacy (%)'].mean())

# 3 Mostre o nome e a região do pais com a maior populacao
print('3 Mostre o nome e a região do pais com a maior populacao')
print(df[df['Population'] == df['Population'].max()][['Country', 'Region']])

# 4 Salve em um csv todos os paises que nao possuem costa maritima (Coastline (coast/area ratio) == 0)
print('4 Salve em um csv todos os paises que nao possuem costa maritima (Coastline (coast/area ratio) == 0)')
print(df[df['Coastline (coast/area ratio)'] == 0].to_csv('paisesSemCosta.csv', sep=';', encoding='utf-8'))
