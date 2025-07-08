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



movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Pulp Fiction"]
for movie in movies:
    print(f"Movie: {movie}")
movies.append("Fight Club")
for movie in movies:
    print(f"Updated Movie List: {movie}")