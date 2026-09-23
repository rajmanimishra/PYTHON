''' if there is a list/tuple or something like this , then we want to find the element present in it  based on the condition'''

n=[1,23,6,5,4,8]
result=tuple(filter(lambda x:x%2==0,n))
print(result)