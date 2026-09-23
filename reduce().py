''' if there is a list/tuple or something like this , then we want to  double the element present in it'''
from functools import reduce
n=[1,23,6,5,4,8]
result=reduce(lambda x,y:x*y,n)
print(result)