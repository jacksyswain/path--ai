print("Hello Jacksy, welcome to AI development!")
name = "Jacksy"
age = 30
is_developer = True
height = 5.9

print(name)
print(age)
print(is_developer)
print(type(height))
print(type(name))
print(type(age))
print(type(is_developer))

newname= input("please enter your name")
print("hello " + newname)
students=["jacksy","kanha","jps","prakash"]
print(students)
print(students[3])
students.append("jyoti")
print(students)
person = {
    "name": "Jacksy",
    "age": 30,
    "role": "developer"
}

print(person["name"])
print(person["role"])
person["country"]="india"
print(person)
myage=31
if myage>18:
    print("you are elegible ")
else:
    print("you are not elegible")

for name in students:
    print(name)