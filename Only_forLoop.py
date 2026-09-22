# iterating over a number list
n=[1,2,3,5,6,55,9,87,7]
for i in n:
    print(i)
   # print(" ")
   
# iterating over list of strings
fruits=["apple","banana","mango","pome","cheese"]   
for fruit in fruits:
    print(fruit)  
    
    
# enumerate function in python --> enumerate()
tasks=["write","test","deploy","kheel","work"]
for index,task in enumerate(tasks):
    print(f" {index}:{task}")