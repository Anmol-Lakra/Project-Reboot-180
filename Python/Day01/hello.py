print("Hello, world"), print()

name = "Lucky"
age = 35
salary = 45000
height = 5.9
is_working = True

print(name)
print(age)
print(salary)
print(height)
print(is_working) 
print()

#We can also print like this
print(name, age, salary, height, is_working)
print()

#type is used to know variable's data type
print(type(name), type(age), type(salary), type(height), type(is_working))
print()

#input function
name = input("Enter your name : ")
print(name)

age = int(input("Enter age : "))
print(age)

print("Enter name, age, salary, height, working or not : ") 
name = input()
age = int(input())
salary = int(input())
height = float(input())
is_working = input("true/false - ")
print(name, age, salary, height, is_working)


