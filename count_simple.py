import datetime

name = str(input("Enter your name: "))
print("Welcome " + name + "\n")
age = str(input("Enter your age: "))
print("Your current age is " + age + "\n")
currentDT = datetime.datetime.now()
print("Current date and time is " + str(currentDT) + "\n")

year = int(currentDT.year) - int(age)

print("You were born in year " + str(year) + "\n")

year = year + 100

print("You will be 100 years old in year " + str(year))

num = str(input("Enter a number between 1 to 10: "))

num_pr = (str(year) + "\n") * int(num)

print(num_pr)
