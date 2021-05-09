import numpy as np

# Numpy Basic Operators
array1 = np.array([1, 2, 3, 4])
array2 = np.array([9, 8, 7, 6])

print("add: ", array1 + array2)
print("sub: ", array1 - array2)
print("sqr: ", array1 ** array2)

print("sin: ", np.sin(array1))

print("Comparison Operators: ", array1 < 2)

array3 = np.array([[1, 2, 3], [4, 5, 6]])
array4 = np.array([[9, 8, 7], [6, 5, 4]])
print("mul: ", array3 * array4)

print("matrix prodcut: ", array3.dot(array4.T))

print(np.exp(array3))

randomArray = np.random.random((5, 5))
print("randomArray: ", randomArray)

print("Np sum: ", randomArray.sum())
print("Np max: ", randomArray.max())
print("Np min: ", randomArray.min())

print("Column :", randomArray.sum(axis=0))
print("Row: ", randomArray.sum(axis=1))

print("sqrt: ", np.sqrt(randomArray))
print("square: ", np.square(randomArray))

print("Np add: ", np.add(randomArray, randomArray))

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(a.dot(b.T))
