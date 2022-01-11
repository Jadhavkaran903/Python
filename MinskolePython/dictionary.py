#Dictionary - Does not store values by index

dictA={
    'name':"karan jadhav",
    'age':26,
    'skills':["python","javaScript","mysql","jquery"],
    'rollNo':42
}

aaa=dictA.get('name')
bbb=dictA['name']

print(aaa)
print(bbb)

for key in dictA:
    print(key,dictA[key])

print("----------------------------------------------")

vehicle={
    'color':"red",
    'types':["sedan","SUV","Hatcback","MUV"]
}

print(vehicle.get('color'))

for x in vehicle.keys():
    print(x)

for x in vehicle.values():
    print(x)

print("----------------------------------------------")

dictB={
    'fn':"Karan Jadhav",
    'rn':[11,44,76]
}

dictC=dictB
dictC['fn']="QA Automation Engineer"
print(dictB)
print(dictC)

print("----------------------------------------------")

dictC=dictB.copy()
dictC['fn']="Full-stack Devloper"

print(dictC)
print(dictB)

print("----------------------------------------------")

dictE={
    'fn':"Karan Jadhav",
    'rn':[11,65,98],
    'age':26
}

# pop - Remove first key and value in dictionary.
dictE.pop('fn')
print(dictE)

# popitem - Remove random key and value in dictionary.
dictE.popitem()
print(dictE)





