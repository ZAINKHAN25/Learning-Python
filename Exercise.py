# name = input("What's your name?")

# age = int(input("Hello " + name + ".Enter your age: "))

# if age < 13:
#     print("You're an child.")
# elif age >= 13 and age < 17:
#     print("You're a teenager .")
# elif age >= 18 and age < 64:
#     print("You're an adult.")
# else:  
#     print("You're a senior citizen.")


# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{num} X {i} = {num * i}")


# num = int(input("Enter a number: "))
# i = 10
# while i >= 1:
#     print(f"{num} X {i} = {num * i}")
#     i -= 1


# def checkifodd(num):
#     if num % 2 != 0:
#         return "It's an odd number."
#     else:
#         return "It's an even number."    
    
# ques = int(input("Enter a number to check if it's odd or even: "))
# print(checkifodd(ques))   



# movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Pulp Fiction"]
# print("Movie List:")
# for movie in movies:
#     print(movie)
# movies.append("Fight Club")
# print("\nUpdated Movie List:")
# for movie in movies:
#     print(movie)


# mainnum = []
# for i in range(1, 6):
#     num = int(input(f"Enter number {i} of 5: "))
#     mainnum.append(num)
# print(mainnum)
# sumofallnum = sum(mainnum)
# average = sumofallnum / len(mainnum)
# largestnum = max(mainnum)
# smallestnum = min(mainnum)
# sortednum = sorted(mainnum)
# print(f"The sum of all numbers is: {sumofallnum}")
# print(f"The average of all numbers is: {average}")
# print(f"The largest number is: {largestnum}, and the smallest number is: {smallestnum}")
# print(f"The sorted list of numbers is: {sortednum}")



# numlist = []
# sortedlist = []
# evenNum = []
# oddNum = []


# for i in range(5):
#     num = int(input(f"Enter number {i + 1} of 5: "))
#     numlist.append(num)

# sortedlist = sorted(numlist)
# for num in sortedlist:
#     if num % 2 == 0:
#         evenNum.append(num)
#     else:
#         oddNum.append(num)

# print(f"The sorted list of numbers is: {sortedlist}")
# print(f"The even numbers are: {evenNum}")
# print(f"The odd numbers are: {oddNum}")


# student = {
#     "name": "",
#     "age": 0,
#     "grade": {
#         "math": 0,
#         "science": 0,
#         "english": 0
#     }
# }

# student["name"] = input("Enter student's name: ")
# student["age"] = int(input("Enter student's age: "))
# student["grade"]["math"] = int(input("Enter student's math grade: "))
# student["grade"]["science"] = int(input("Enter student's science grade: ")) 
# student["grade"]["english"] = int(input("Enter student's english grade: "))

# average_grade = (student["grade"]["math"] + student["grade"]["science"] + student["grade"]["english"]) / 3
# print(f"\nStudent Name: {student['name']}")
# print(f"Student Age: {student['age']}")
# print(f"Math Grade: {student['grade']['math']}")
# print(f"Science Grade: {student['grade']['science']}")
# print(f"English Grade: {student['grade']['english']}")
# print(f"Average Grade: {average_grade:.0f}")