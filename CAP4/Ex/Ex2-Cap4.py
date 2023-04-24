import numpy as np

np.random.seed(5)

#1
# Array de numeros aleatorios entre 0 e 1 multiplicado por 100 e convertido para int
arr = np.random.randn(10)
print(f'Array: {arr}')
arr2 = arr*100
print(f'Array * 100: {arr2}')
arr3 = arr2.astype(int)
print(f'Array int: {arr3}')

#2
# Matriz de 4x4 de numeros inteiros aleatorios entre 1 e 50
matrix = np.random.randint(1, 50, (4, 4))
print(f'Matrix: {matrix}')

#3
# Media das linhas da matriz
print(f'Media das linhas: {np.average(matrix, axis=1)}')
# Media das colunas da matriz
print(f'Media das colunas: {np.average(matrix, axis=0)}')
# Maior media das linhas
print(f'Maior media das linhas: {np.max(np.average(matrix, axis=1))}')
# Maior media das colunas
print(f'Maior media das colunas: {np.max(np.average(matrix, axis=0))}')

#4
# Counter de valores unicos da matriz
print(f'Counter: {np.unique(matrix, return_counts=True)}')
# Valores que aparecem 2 vezes
print(f'Valores que aparecem 2 vezes: {np.unique(matrix, return_counts=True)[0][np.unique(matrix, return_counts=True)[1] == 2]}')

