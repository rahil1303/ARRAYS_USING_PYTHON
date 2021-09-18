from arrays import *
arr1 = array("i",[1,2,3,4,5,6,7,8])
print(arr1)


def tranversearray(array):
  for i in array:
    print(i)
  traversearray(arr1)

  
def accessElement(array,index):
    if index >= len(array):
        print("There is not any element in this index")
    else:
        print(array[index])

accessElement(arr1,4)

def searchelement(array,value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The element does not exist in this array"
print(searchelement(arr1,5))



arr1.remove(2)
print(arr1)
