#Завдання 1
a = 0
while a < 21 :
    n = int(input("Enter the number:"))
    print(n >= 100)
    a += 1

#Завдання 2
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

if num1 > num2:
    print("Найбільше число:", num1)
else:
    print("Найбільше число:", num2)

#Завдання 3
input_str = input("Введіть рядок: ")

if input_str == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif input_str == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", input_str + "!")

#Завдання 4
income = float(input("Введіть річний дохід: "))

tax = 0

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

tax = max(tax, 0)  # Податок не може бути меншим за нуль

tax = round(tax)  # Заокруглення до цілих талерів

print("Податок становить:", tax, "талерів")

#Завдання 5
year = int(input("Введіть рік: "))

if year >= 1582:
    if year % 4 != 0:
        result = "Common year"
    elif year % 100 != 0:
        result = "Leap year"
    elif year % 400 != 0:
        result = "Common year"
    else:
        result = "Leap year"
else:
    result = "Not within the Gregorian calendar period."

print(result)

#Завдання 6
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess = int(input("Enter an integer number: "))

while guess != secret_number:
    print("Ha-ha! You're stuck in my loop!")
    guess = int(input("Try again. Enter another number: "))

print("Well done, muggle! Now you are free!")

#Завдання 7
import time

# Write a for loop that counts to five.
for i in range(1, 6):
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    print(i, "Mississippi")
    # Body of the loop - use: time.sleep(1)
    time.sleep(1)

# Write a print function with the final message.
print("Ready or not, here I come!")

#Завдання 8
# Start an infinite loop
while True:
    # Ask the user to enter a word
    word = input("Enter a word: ")

    # Check if the word is "chupacabra"
    if word == "chupacabra":
        # If it is, print a message and break the loop
        print("You've successfully left the loop.")
        break

#Завдання 9
# Ask the user to enter a word
user_word = input("Enter a word: ")

# Convert the user's word to uppercase
user_word = user_word.upper()

# Iterate over each letter in the word
for letter in user_word:
    # Check if the letter is a vowel
    if letter in ['A', 'E', 'I', 'O', 'U']:
        # If it is, continue to the next iteration
        continue
    # If it's not a vowel, print the letter on a separate line
    print(letter)

#Завдання 10
# Prompt the user to enter a word and convert it to uppercase
user_word = input("Enter a word: ").upper()

# Initialize an empty string to store the word without vowels
word_without_vowels = ""

# Iterate over each letter in the user's word
for letter in user_word:
    # Check if the letter is a vowel
    if letter in ['A', 'E', 'I', 'O', 'U']:
        # If it is, continue to the next iteration
        continue
    # If it's not a vowel, add it to the word_without_vowels
    word_without_vowels += letter

# Print the word without vowels
print(word_without_vowels)

#Завдання 11
# Prompt the user to enter the number of blocks
num_blocks = int(input("Enter the number of blocks: "))

# Initialize variables
height = 0
layer_blocks = 1
blocks_used = 0

# Build the pyramid
while blocks_used + layer_blocks <= num_blocks:
    height += 1
    blocks_used += layer_blocks
    layer_blocks += 1

# Print the height of the pyramid
print("The height of the pyramid is:", height)

#Завдання 12
# Prompt the user to enter a natural number
c0 = int(input("Enter a natural number: "))

# Initialize the step counter
steps = 0

# Calculate the Collatz sequence
while c0 != 1:
    print(c0)
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    steps += 1

# Print the final value of c0 and the number of steps taken
print(c0)
print("Number of steps:", steps)