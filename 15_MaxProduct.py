mylist = list(map(int,input("\n Enter the input values as a list").split().strip()))
def findmaxproduct(array):
  maxproduct = 0
  for i in range(len(array)):
    for j in range(i+1,len(array)):
      if array[i] * array[j] > maxproduct:
        maxproduct = array[i] * array[j]
        pairs = str(array[i]) + "," + str(array[j])
        
findmaxproduct(mylist)
