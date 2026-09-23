"""Functions are the reusable block of codes which are used for the particular task"""

#Ques. function to add two number
def add(a,b):
    return a+b

print(add(2,3))

#
# without returning
def add(a,b):
    print (a+b)

add(2,3)


"""(args)Multiple positional argumernts"""
def add(* num):
    print(sum(num))
add(10,20,30)



"""(kwargs)Multiple keyword argumernts"""
def data(** num):
    print(num)
data( name="RAjmani",age=22)


