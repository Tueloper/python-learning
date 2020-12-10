import math
import converter

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
