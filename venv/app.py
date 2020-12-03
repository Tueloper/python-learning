import math

# Name variables
name = 'John Smith'
age = 20
price = 10
rating = 0.4
is_ready = False
is_exist = True
sentence = name + ' is'
sentence = """
This is a python course

As we dey learn am 

Baba God go bless our hustle 
"""
# python template literal
message = f'{name} is {20} years old and is a {is_exist} member'

# Function calls
# name = input('What is Your Name? ')
# color = input('What is Your Favorite Color? ')
# print(name + ' likes ' + color)

# More logics
# birth_year = input('Birth year: ')
# age = 2020 - int(birth_year)

# Classwork
# ask_weight = input('What is your weight (lbs)? ')
# user_weight = int(ask_weight) * 0.45
# print(sentence[1:-9])
# print(message.upper())
# print(message.find('y'))
# print(message.replace("years", "Some Years"))
# print ('years' in message)
# print(message.title())
# print(message)
# print(len(message))

# SO Python makes use of BODMAS for calculation
# The precedence is as follows
# parenthesis - exponentiation - multiplication/division - addition/subtraction

# more number methods call
# x = 4.09
# print(round(x))
# print(abs(-889.0))
# print(math.ceil(2.7))
# print(math.floor(3.77))
# print(math.trunc(7.8892))
# print(math.degrees(45))

# conditionl statements
# is_hot = False
# is_cold = False
# if is_hot:
#     print("It's a hot day")
# elif not is_hot:
#     print("It's a cold day")
# else:
#     print('Calm day')
#
# land_price = 10000000
# buyer_good_credits = False
# price = land_price
#
# if buyer_good_credits:
#     discount = 0.1 * land_price
# else:
#     discount = 0.2 * land_price
# print(f"${round(land_price - discount)}")

# exercise

# weight_input = int(input('Weight: '))
# weight_type = input('(L)bs or (K)g: ')
# user_weight = 0
#
# if weight_type.upper() == 'L':
#     correct_weight = weight_input * 0.45
#     print(f"You weigh {correct_weight} kilos")
# else:
#     correct_weight = weight_input // 0.45
#     print(f"You weigh {correct_weight} pounds")


# Guess game
# guess_number = 9
# guess_count = 0
# guess_limit = 3
#
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == guess_number:
#         print('Yaaay You Guessed Right')
#         break
# else:
#     print('Sorry You Failed')

# Car manual guide
# i = 1
# manual = '''
# start - To start the car
# stop - To stop the car
# quit - To Exit
# '''
# start = 'Car started... Ready to go!'
# stop = 'Car stopped'
# unkown = "I don't understand that..."
#
# while True:
#     input_value = input('> ').upper()
#     if input_value == 'HELP':
#         print(manual)
#     elif input_value == 'START':
#         print(start)
#     elif input_value == 'STOP':
#         print(stop)
#     elif input_value == 'QUIT':
#         break
#     elif input_value != 'START' or input_value != 'STOP' or input_value != 'QUIT':
#         print(unkown)

#  loops
# prices = [10, 20, 30, 40, 50]
# sum = 0
# for item in prices:
#     sum += item
# print(sum)

# nested loops
# for x in range(5):
#     for y in range(10):
#         print(f"({x}, {y})")

# numbers = [2, 2, 2, 2, 10]
#
# for items in numbers:
#     result = ''
#     for item in range(items):
#         result += 'x'
#     print(result)

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mar']
# print(names[2:-1])

# numbers = [2, 3, 422, 5, 7, 10, 67]
# max = numbers[0]
#
# for item in numbers:
#     if item > max:
#         max = item
# print(max)

# matrix = [
#     [2, 3, 2],
#     [7, 3, 0],
#     [1, 4, 6]
# ]
#
# for row in matrix:
#     for item in row:
#         print(item)

# numbers = [2, 1, 4, 6, 7, 0, 9]
# # print(numbers.pop())
# numbers.insert(0,10)
# numbers.remove(10)
# numbers.sort()
# numbers.reverse()
# numbers.copy()
#
# print(numbers)

# numbers = [2, 9, 4, 2, 7, 7, 9]
# dup = numbers[0]
# uniques = []
# for item in numbers:
#     if (item == dup):
#         numbers.remove(item)
#     else:
#         dup = item

# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# Dictionaries in Python
# dictionaries are like objects
# keys should be unique
# customer = dict(name="John Smith", age=30, is_verified=True)
# customer["is_ready"] = True
# print(customer.get("name"));

messagee = input(">")
words = messagee.split(" ")
digits = {
    "1": "One",
    "2": "two",
    "3": "Three"
}

emojis = {
    ":)": ":grinning:",
    ":(": ":tired_face:"
}

output = ''
for word in words:
    output += emojis.get(word, word) + " "

print(output)

# input(Numbers)
