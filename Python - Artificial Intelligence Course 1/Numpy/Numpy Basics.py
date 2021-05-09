import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])  # 1*15 vector

print("shape: ", array.shape)
newArray = array.reshape(3, 5)
print("newArray: ", newArray)
print("newArrayShape: ", newArray.shape)
print("Dimension: ", newArray.ndim)  # Dimension (Dizi kaç boyutlu)

print("Type of Data in The Array: ", newArray.dtype.name)
print("Size Array: ", newArray.size)

print("Type: ", type(newArray))

newArray2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 5]])
print("newArray2: ", newArray2)

zerosArray = np.zeros((3, 4))
print("zeros: ", zerosArray)

zerosArray[0, 0] = 5
print(zerosArray)

onesArray = np.ones((3, 4))
print("onesArray: ", onesArray)

emptyArray = np.empty((3, 4))
print("emptyArray", emptyArray)

arangeArray = np.arange(10, 50, 5)
print("arangeArray: ", arangeArray)

linspaceArray = np.linspace(10, 50, 20)
print("linspaceArray: ", linspaceArray)

