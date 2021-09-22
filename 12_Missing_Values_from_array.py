#### Linear Search
Over here we basically find the two sums of the values and then subtract them.
mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,6,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
def missingvalue(list,n):
    sum1 = 50*51/2
    sum2 = sum(list)
    print(sum1-sum2)
    
n = input()
missingvalue(mylist,50)
