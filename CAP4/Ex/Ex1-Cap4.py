import numpy as np
#1
linearlist = np.linspace(0, 1, 21)
print(f'Linear list: {linearlist}')

#2
pairlist = np.arange(0, 51, 2)
pairlist2 = np.arange(100, 50, -2)
concatPairList = np.concatenate((pairlist, pairlist2))
concatPairList = np.sort(concatPairList)
print(f'Pair list: {concatPairList}')

#3
concatPairList = np.flip(concatPairList)
print(f'Pair list rev: {concatPairList}')

#4
onesMatrix = np.ones([3, 4])
onesList = np.reshape(onesMatrix, onesMatrix.size)
print(f'Ones: {onesList}')

#5
x,y = input("Enter with the range of the matrix (ex: 1 2): ").split()
matrix = np.ones([int(x), int(y)])
print(f'Matrix: {matrix}')
if matrix.size % 2 == 0:
    print(f'Even')
else:
    print(f'Odd')