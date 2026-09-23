#creating the sets
sets={1,2,3,45,6,4,5,45};
for i in sets:
    print(i)
    
    
print(sets)
print(type(sets))




"""Operations in sets"""

print(sets.add(20))
print(sets) # add the element at right position
print(sets.pop())# popping the element from the front 
print(sets)

setss={12,36,54,8,98,78,2}
print(sets.union(setss)) # giving the all element
print(sets.intersection(setss))# giving only element present in both the sets



