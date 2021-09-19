### In this assignment we will do the following tasks:
# 1. CREATE AN ARRAY AND TRAVERSE

from array import *
arr1 = array("i",[1,2,3,5,4,6,7,8])
print(arr1)

def traversefunc(array):
    for i in array:
        print(i)
print(traversefunc(arr1))

# 2. ACCESS INDIVIDUAL ELEMENTS THROUGH indexes

print("Step 2")
print(arr1[1])

# 3. APPEND ANY VALUE TO THE ARRAY USING APPEND METHOD()

print("Step 3")
arr1.append(7)
print(arr1)

# 4. INSERT VALUE IN AN ARRAY USING INSERT METHOD()

print("step 4")
arr1.insert(3,9)
print(arr1)

# 5. EXTEND PYTHON ARRAY USING EXTEND METHOD()

print("Step 5")
arr2 = array("i", [10,11,12,13,14,15])
arr1.extend(arr2)
print(arr1)

# 6. ADD ITEMS FROM A LIST INTO ARRAY USING FROMLIST() METHOD

print("Step 6")
templist = [20,21,22,23,24,25]
arr1.fromlist(templist)
print(arr1)

# 7. REMOVE ANY ARRAY ELEMENT USING REMOVE() METHOD

print("Step 7")
arr1.remove(7)
print(arr1)

# 8. REMOVE LAST ARRAY ELEMET USING POP() METHOD

print("Step 8")
arr1.pop(8)
print(arr1)

# 9. FETCH ANY ELEMENT THROUGH ITS INDEX USING INDEX() METHOD

print("Step 9")
print(arr1.index(23))

# 10. REVERSE AN ARRAY USING REVERSE() METHOD

print("Step 10")
arr1.reverse()
print(arr1)
# 11. GET ARRAY BUFFER INFORMATION THROUGH BUFFER_INFO() METHOD

print("Step 11")
print(arr1.buffer_info())
print(arr1)

# 12. CHECK FOR NUMBER OF OCCURRENCES OF AN ELEMENT USING COUNT() METHOD

print("Step 12")
print(arr1.count(7))
print(arr1.count(6))

# 13. CONVERT ARRAY TO A STRING USING TOSTRING() METHOD

print("Step 13")
strtemp = arr1.tostring()
print(strtemp)
ints = array("i")
ints.fromstring(strtemp)
print(ints)

# 14. CONVERT AN ARRAY TO A PYTHON LIST WITH SAME ELEMENTS USING TOLIST() METHOD

print("Step 14")
print(arr1.tolist())

# 15. APPEND A STRING TO CHAR ARRAY USING FROMSTRING() METHOD 


# 16. SLICE THE ELEMENTS FROM AN ARRAY

print("Step 16")
print(arr1[::-1])


