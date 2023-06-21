import pandas as pd
import numpy as np

# Series é um array unidimensional que pode armazenar qualquer tipo de dado
# Series é uma coluna de um DataFrame
# Series é um array com índices customizados

# Criando uma Series
series = pd.Series({'a': 1, 'b': 2, 'c': 3})
series2 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(series2.add(series, fill_value=0))
print(series[['b', 'c']]) # Slice em Series
print(series[(series > 1) & (series < 3)]) # Filtro em Series

# DataFrame é uma estrutura de dados tabular bidimensional
# DataFrame é uma tabela de dados
# DataFrame é um conjunto de Series

# Criando um DataFrame
df = pd.read_csv('paises.csv', delimiter=';', encoding='utf-8')
print(df.columns) # Colunas do DataFrame
# Printar todas as informações da Irlanda
print(df[df['Country'].str.startswith('Ireland')])
