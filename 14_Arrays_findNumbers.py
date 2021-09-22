def findnumber(array,number):
  for i in range(len(array)):
    if array[i] == number:
      print(i)
mylist = list(map(int,input("\n Enter the input list").strip().split())))
a = int(input())
findnumber(mylist,a)
