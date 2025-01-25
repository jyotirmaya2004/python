#operations on arrays
from array  import *
#create an array with int values
arr = array('i',[10,20,30,40,50,60])
print("Original array :",arr)

# append 80 to array 
arr.append(80)
print("After appending '80' :",arr)
arr.insert(6,90)
print("After inserting 90 :",arr)

arr.remove(90)
print("After removing 90 :",arr)

#remove last element using pop()
n=arr.pop()
print("Array after using pop() :",arr)
print("Popped element :",n)