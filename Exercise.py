name = input("What's your name?")

age = int(input("Hello " + name + ".Enter your age: "))

if age < 13:
    print("You're an child.")
elif age >= 13 and age < 17:
    print("You're a teenager .")
elif age >= 18 and age < 64:
    print("You're an adult.")
else:  
    print("You're a senior citizen.")