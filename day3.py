import random
import math

print(math.sqrt(16))

print(random.randint(1,10))

name = input("hey can yoy share your name: ")
age = int(input("hey would you like to share your age: "))
corse= input("hey can you share the corse you are intrest in: ")

def greet(name,age,corse ):
    print("hello ", name , " you are ", age, "years old and as we know you are intrested on ", corse )

greet(name,age,corse) 

def square(num):
    return num*num

print(square(9))

def check_even(age):
    if age%2==0:
        print("you are at even age")
    else:
        print("you are at odd age ")

check_even(age)