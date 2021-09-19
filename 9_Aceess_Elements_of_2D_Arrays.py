
import numpy as np

newarr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(newarr)

new2Darr = np.insert(newarr,0,[[17,18,19,20]],axis = 0) ### Array
print(new2Darr)

new2Darr = np.insert(newarr,0,[[21,22,23,24]],axis = 1) ### Column
print(new2Darr)

def acessElements(array,rowIndex,columnIndex):
  if rowIndex >= len(array) and columnIndex >= len(array[0]):
    print("The inncorect Index")
  else:
    print(array[rowIndex][columnIndex])
acessElements(new2Darr,2,2)
