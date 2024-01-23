list = ["Ice-cream", "hotdog", "coffee"]

print(list)

list[0] = "Chocolate"

list.append("Biscut")
list.pop()
list.sort()
list.insert(1, "hamburger")
list.clear()
for i in list:
    print(i)
    
    
    
# tuple

tuple = ("Apex", 21 ,"Apex" , "Hub")

print(tuple.count("Apex"))
print(tuple.index("Apex"))
for i in tuple:
    print(i)
    
    
# set 

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup","knife"}
# utensils.add("napkin")
# utensils.remove("fork")

# utensils.update(dishes)
print(utensils.difference(dishes))
print(utensils.union(dishes))
print(utensils.intersection(dishes))
print(utensils)



#Dictionary


dist = {
    "name" : "ANi",
     "age" : 21
}
print(dist.get('age'))
print(dist['name'])
dist.update({'Subject':'Computer'})
dist.pop('name')
print(dist.keys())
print(dist.values())
print(dist.items())