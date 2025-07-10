# print("Hello World!")


# name = "Zain Khan"
# print("Hey name is " + name)


# isZain = False
# if isZain == True:
#     print("Welcome Back Zain")
# else:
#     print("Hello stranger")


# name = ["Zain", "Khan", "Zain Khan"]
# print(name[0])


# cities = ["Atlanta", "Baltimore", "Chicago",
# "Denver", "Los Angeles", "Seattle"]
# print(cities[0])
# cities.append("New York")
# print(cities[6])


# cities = ["Atlanta", "Baltimore", "Chicago",
# "Denver", "Los Angeles", "Seattle"]
# cities.insert(0, "New York")
# print(cities[0])


# cities = ["Atlanta", "Baltimore", "Chicago",
# "Denver", "Los Angeles", "Seattle"]
# updateCities = cities[1:]
# print(updateCities)


# tasks = ["email Frank", "call Sarah", "meet with Zach"]
# del tasks[1]
# tasks.remove(tasks[0])
# print(tasks)
# tasks = ["email Frank", "call Sarah", "meet with Zach"]



# name = input("What's your name? ")
# print("Hello, " + name + "!")


# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You're an adult.")
# else:
#     print("You're a minor.")


# for i in range(5):
#     print(i)


# count = 0
# while count < 5:
#     print(count)
#     count += 1


# def greet(name):
#     print("Hello, " + name + "!")
# greet("Zain")



# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num)



# numbers = [5, 2, 9, 1, 7]
# sorted_list = sorted(numbers)
# print(numbers)           
# print(sorted_list)      
# min_val = min(numbers)
# max_val = max(numbers)
# print(min_val, max_val)



# student = {
#     "name": "Your Name",
#     "age": 0,
#     "grade": {
#         "math": 0,
#         "science": 0,
#         "english": 0
#     },
#     "subject": "None"
# }
# for key,value in student.items():
#     print(key, ":", value)


import random
print(random.randint(1, 100))  # Generates a random integer between 1 and 100
print(random.choice(['apple', 'banana', 'cherry']))  # Randomly selects an item from the list
print(random.sample(range(1, 100), 5))  # Randomly selects
print(random.shuffle([1, 2, 3, 4, 5]))  # Randomly shuffles the list