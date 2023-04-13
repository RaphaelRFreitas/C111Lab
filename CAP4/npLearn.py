import numpy as np

#Criando um numpy array aleatório
np.random.seed(5)
arr = np.random.randint(0, 10, 10)
print(f'Array: {arr}')