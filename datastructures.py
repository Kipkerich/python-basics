# Tuples
names=("Jacob", "Wayne", "Caleb", "Elizabeth", "Grace", "Sophie")
print(names[3])
print(names[5])
print(names[0:3])
print(names[3:5])
print(names[2:])

for jina in names:
    print(jina)
# Lists
cars=["Mercedes", "Audi", "Subaru", "Nissan", "Toyota", "Mazda"]

print(cars[0])
print(cars[5])
print(cars[0:3])
print(cars[3:5])
print(cars[2:])

for gari in cars:
    print(gari)
# Manipulating items in a list
cars[0]="Bugatti"
print(cars)
# Dictionaries
students={"adm1":"Michael", "adm2":"Charity", "adm3":"Chris"}
print(students["adm2"])
print(students.values())
print (students.keys())

for x in students.values():
    print(x)
for y in students.keys():
    print(y)
# Sets
marks= {30,50,45,30,65,90,45,75,65,50,45,90}
print(marks)
