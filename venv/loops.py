#  loops
prices = [10, 20, 30, 40, 50]
sum = 0
for item in prices:
    sum += item
print(sum)

# nested loops
for x in range(5):
    for y in range(10):
        print(f"({x}, {y})")

numbers = [2, 2, 2, 2, 10]

for items in numbers:
    result = ''
    for item in range(items):
        result += 'x'
    print(result)

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mar']
print(names[2:-1])

numbers = [2, 3, 422, 5, 7, 10, 67]
max = numbers[0]

for item in numbers:
    if item > max:
        max = item
print(max)

matrix = [
    [2, 3, 2],
    [7, 3, 0],
    [1, 4, 6]
]

for row in matrix:
    for item in row:
        print(item)

numbers = [2, 1, 4, 6, 7, 0, 9]
# print(numbers.pop())
numbers.insert(0,10)
numbers.remove(10)
numbers.sort()
numbers.reverse()
numbers.copy()

print(numbers)

numbers = [2, 9, 4, 2, 7, 7, 9]
dup = numbers[0]
uniques = []
for item in numbers:
    if (item == dup):
        numbers.remove(item)
    else:
        dup = item

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# Dictionaries in Python
# dictionaries are like objects
# keys should be unique
customer = dict(name="John Smith", age=30, is_verified=True)
customer["is_ready"] = True
print(customer.get("name"));
