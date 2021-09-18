from arrays import *

arr1 = array("i",[1,2,5,4,3])
def searchelement(array,value):
  for i in array:
    if i == value:
      return array.index(value)
    return "The element does not exist"
  
  searchelement(arr1,5)
