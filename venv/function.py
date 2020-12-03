def greet_user(first_name, last_name):
    print('Hi there!!')
    print(f"hi {first_name} {last_name}")
    print('Welcome abroad')

greet_user("John", "Smith")

# function to calculate a square of a number
def square(num):
    return num * num

print(square(3))


emojis = {
    ":)": ":grinning:",
    ":(": ":tired_face:"
}

def emoji_generator():
    messagee = input(">")
    words = messagee.split(" ")
    output = ''
    for word in words:
        output += emojis.get(word, word) + " "
    return output

print(emoji_generator())
