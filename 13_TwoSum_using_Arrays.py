def findpairs(nums,target):
	for i in range(len(nums)):
		for j in range(i+1,len(num)):
			if num[i] == num[j]:
				continue
			elif num[i] + num[j] = target:
				print(i,j)

mylist = list(map(int,input("\n Enter the input list").strip().split())) 
a = int(input())
findpairs(mylist,a)
