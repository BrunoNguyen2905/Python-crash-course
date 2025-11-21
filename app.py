import math

x = 1
y = 2
unit_price = 2
word = "hello World"
second_word = "Python \"Programming"
word_with_spaces = "   hello World   "
# concat_word is
concat_word = f"{word} {second_word}"
mix_type = f"{len(second_word)} {x + y} {unit_price}"
print("word:", word)
print("mix_type:", mix_type)
print("second_word:", second_word)
print("concat_word:", concat_word)
print("Sum:", x + y + unit_price)
print("Length:", len(word))
print("First character:", word[0])
print("Last character:", word[-1])
print("Substring (0-5):", word[0:5])
print("Substring (0-):", word[0:])
print("Substring (-5):", word[:5])
print("Substring (-):", word[:])
print("Substring (1-(-1)):", word[1:-1])
print("Uppercase:", word.upper())
print("Lowercase:", word.lower())
print("Title Case:", word.title())
# Demonstrating string operations and f-strings in Python
print("Trimmed:", word_with_spaces.strip())
print("Left Trimmed:", word_with_spaces.lstrip())
print("Right Trimmed:", word_with_spaces.rstrip())
print("find 'World':", word.find("Wor"))
print("find 'world':", word.find("wor"))
print("Replaced 'World' with 'Universe':", word.replace("World", "Universe"))
# The line `print("in operator 'hello' in word:", "hello" in word)` is checking if the substring
# "hello" is present in the string variable `word`.
print("in operator 'hello' in word:", "hello" in word)
print("not in operator 'hello' not in word:", "hello" not in word)
print("Count 'l' in word:", word.count("l"))
print("10 + 3 =", 10 + 3)
print("10 - 3 =", 10 - 3)
print("10 * 3 =", 10 * 3)
# Standard division gives a float result
print("10 / 3 =", 10 / 3)
# Floor division gives the integer part of the division
print("10 // 3 =", 10 // 3)
# Modulus operator gives the remainder of the division
print("10 % 3 =", 10 % 3)
# Exponentiation operator raises 10 to the power of 3
print("10 ** 3 =", 10 ** 3)

x = 10
x += 3  # simpler syntax than x = x + 3
print("x after x += 3:", x)
print("round", round(10 / 3, 2))  # Rounds the result to 2 decimal places
print("abs", abs(-7))  # Absolute value

print("math ceil", math.ceil(4.2))  # Rounds 4.2 up to the nearest integer
print("math floor", math.floor(4.7))  # Rounds 4.7 down to the nearest integer
print("math sqrt", math.sqrt(16))  # Square root of 16

x = input("Enter a number X: ")
print("typeof x:", type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")
# int(x)
# float(x)
# str(x)
# bool(x)
# Falsy: "", 0, 0.0, [], {}, None, False
# Truthy: "hello", 1, -1, [1, 2], { "key": "value" }, True


temprature_celsius = float(input("Enter temperature in Celsius: "))
if temprature_celsius > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temprature_celsius > 20:
    print("It's a nice day")
else:
    print("It's cold day")
    print("Wear warm clothes")
print("Done")


age = int(input("Enter your age: "))
# if age >= 18:
#     message = "You are an adult"
# else:
#     message = "You are a minor"
# clearner way to write the above if-else statement
message = "You are an adult" if age >= 18 else "You are a minor"
print(message)

# logical operators: and, or, not

your_income = int(input("Enter your income: "))
while True:
    credit_input = input("Do you have good credit? (yes/no): ").strip().lower()
    if credit_input in ("yes", "no"):
        has_good_credit = credit_input == "yes"
        break
    print("Please answer 'yes' or 'no'.")

# deal_message = "Eligible for loan" if (
#     your_income > 50000 and has_good_credit) else "Not eligible for loan"
is_student = age <= 18
if your_income > 50000 and has_good_credit and not is_student:
    deal_message = "Eligible for loan"
elif (your_income > 50000 or has_good_credit) and not is_student:
    deal_message = "Eligible for half loan"
else:
    deal_message = "Not eligible for loan"

print(deal_message)

# age >= 18 and age < 65 is the same as 18 <= age < 65
if 18 <= age < 65:
    print("You are eligible for work")
else:
    print("You are not eligible for work")

for number in range(6):
    print("Attempt from 0 to 6", number, number * ".")

for number in range(1, 6):
    print("Attempt from 1 to 6", number, number * ".")

for number in range(1, 10, 2):
    print("Attempt from 1 to 10 with 2 gap", number, number * ".")

success = False
for number in range(3):
    print("Attempt", number)
    # if number == 2:
    #     success = True
    if success:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

for x in range(1, 5):
    for y in range(1, 3):
        print(f"({x}, {y})")

print("Type of 5:", type(5))
print("Type of range", type(range(5)))

# Iterable:
for x in range(5):
    print("Number:", x)
for item in "Python":
    print("Character:", item)
for y in [1, 2, 3]:
    print("List item:", y)

shopping_cart = [
    ("apple", 10, 0.5),
    ("banana", 5, 0.25),
    ("orange", 8, 0.75)
]
sum = 0
for item, quantity, price in shopping_cart:
    total = price * quantity  # assuming each item costs 2 units
    print(f"{item}: {quantity}, Price: ${total}")
    sum += total
print("End of program")
print("Total price:", f"${sum}")

totalEvenNumbers = 0
for x in range(1, 10):
    if x % 2 == 0:
        print("Even number:", x)
        totalEvenNumbers += 1

print(f"We have {totalEvenNumbers} even numbers.")

# Function: A block of code that performs a specific task, all functions return None by default unless a return statement is used.
# Two main types of functions:
# 1- Perform a task
# 2- Return a value

# 1- Perform a task


def greet_user(name):
    print(f"Hello, {name}!")


greet_user("Alice")

# 2- Return a value


# all required parameters must be provided before optional parameters
def square_then_plus(number, plus=2):
    return number * number + plus


print("Squared value:", square_then_plus(number=5))

# square brackets to create list of arguments [2, 3, 4, 5]
# parentheses to create tuple of arguments  (2, 3, 4, 5) (tuple is similar to list but it is a collection of objects which cannot be changed/modified)


def multiply(*numbers):
    result = 1
    for number in numbers:
        print("number:", number)
        result *= number
    print("Result inside function:", result)
    return result


multiply(2, 3, 4, 5)


# Before pushing to a repository,
# export dependencies: pip freeze > requirements.txt

# When dowloading/cloning a project,
# Create virtual environment: python -m venv env
# Activate virtual environment: source env/bin/activate (macOS/Linux)
#                          .\env\Scripts\activate (Windows)
# Install dependencies: pip install -r requirements.txt
# Deactivate virtual environment: deactivate
