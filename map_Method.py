''' if there is a list/tuple or something like this , then we want to  double the element present in it'''

n=[1,23,6,5,4,8]
result=tuple(map(lambda x:x*2,n))
print(result)