import numpy as np

#Criando um numpy array aleatório
np.random.seed(5)
arr = np.random.randint(1, 10, 10)
print(f'Array: {arr}')
#valores unicos mantendo a ordem
arrOrd = np.unique(arr, return_index=True)
print(f'Array ordenado: {arrOrd}')
print(sorted(arrOrd[0], key=lambda x: arrOrd[1][arrOrd[0].tolist().index(x)]))

#Criando martriz 3x3
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(np.average(matrix))