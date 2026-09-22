"""There are many list operations 
1.accessing list
2.traverse through loop
3.update index
4.slicing
"""

list1=['1',"S", "Rajmani"]
  
for i in list1:
    print(i)


print(list1[1]) # printing & accessing 1 index
print(list1[-1])# accessing last index
list1[0]=2 # modified the previous value
print(list1[0])

print(len(list1))# printing the length of the list1

print(list1[0:3]) # slicing the list1