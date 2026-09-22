# Dictionary creation 
student={
    "name":"Rajmani Mishra",
    "course":"Btech",
    "rollno":55,
    "age":24,
    
}
print(student.get("ages"))# no error with get keyword
print(student["age"])


"""Dictionary Operations"""
print(student.keys())
print(student.values())


# adding new element
student["city"]="Lucknow"

print(student.keys())
print(student.values())

# update the values
student["city"]="Gorakhpur"

print(student.keys())
print(student.values())

# delete the items
del student["course"]

print(student.keys())
print(student.values())


# pop()
print(student.pop("age"))

print(student.keys())
print(student.values())



print(student.items())



# .keys(),.values(),.items(),.get()--> ye sb methods hai dictionary ke


