# class is defined here
class Student:
    clg_name="RR Institute of Modern Technology"
    
    # constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
s1=Student("Rajmani Mishra",97) # object creation
print(s1.name,s1.marks)#printing the object