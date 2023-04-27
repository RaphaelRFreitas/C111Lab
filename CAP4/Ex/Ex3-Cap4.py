import numpy as np

dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')
print(dataset[0])
#1
# Porcentagem de missões que foram bem sucedidas
print(f'Porcentagem de missões que foram bem sucedidas: {np.average(dataset[1:, 7]=="Success")*100}%')

#2
# Média de gastos das missões if cost is > 0
cond = dataset[1:, 6].astype(float) > 0
print(f'Média de gastos das missões: {np.average(dataset[1:, 6].astype(float)[cond])} Milhoes USD')

#3
# N de missões que foram feitas pelos EUA
cond = np.char.find(dataset[1:, 2], 'USA')
print(f'N de missões que foram feitas pelos EUA: {np.count_nonzero(cond != -1)}')

#4
# Mais cara feita pela SpaceX
cond = np.char.find(dataset[1:, 1], 'SpaceX')
print(f'Mais cara feita pela SpaceX custou: {np.max(dataset[1:, 6].astype(float)[cond])} Milhoes USD')

#5
# N de missões feitas por cada empresa
for i in np.unique(dataset[1:, 1]):
    cond = np.char.find(dataset[1:, 1], i)
    print(f'N de missões feitas pela {i}: {np.count_nonzero(cond != -1)}')