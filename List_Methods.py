""" Basic methods of the list are
1.append()
2.extend()
3.pop()
4.sort()
5.copy()
"""

num=[1,2,"fruits",'0',"Rajmani Mishra"]

num.append(50) # adding element 50 to the list
for i in num:
    print(i)
    
    
print("Extending list")
num.extend([60,70,80])# extending the list
for i in num:
    print(i)


num.pop() # removing the last element
for i in num:
    print(i)
    
# num.sort()
# for i in num:
#     print(i)


    
