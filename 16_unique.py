mylist = [1,2,3,4,5,5,5,6,7,8,9]
def isunique(list):
    a = []
    for i in list:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True

isunique(mylist)
