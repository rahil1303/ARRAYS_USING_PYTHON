from arrays import *
arr1 = array("i",[1,2,3,4,5,6,7,8])
#### Insert values into array
arr1.insert(5,8)

def traversearray(array):
  for i in array:
    print(i)
  
  traversearray(arr1)
  

 def accesselements(array,index):
  if index >= len(array):
    print("There is no number in the provided index")
  else:
    print(array[index])
    
  accesselements(arr1,5)
