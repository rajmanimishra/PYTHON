"""List comprehension is basically a one line so;ution to a problem"""

"""Quest. print number 1 to 6"""

# using list
numbers=[]

for i in range(1,7):
    numbers.append(i)
print(numbers)


# using list comrehension

numberss=[i for i in range(1,7)]
print(numberss)

"""Ques. write the even number"""
# using list comrehension

even=[i for i in range(1,11)if i%2==0]
print(even)