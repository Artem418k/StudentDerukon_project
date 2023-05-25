#Приклад 1
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

user_input = input("Введіть текст: ")
if is_palindrome(user_input):
    print("Це паліндром!")
else:
    print("Це не паліндром.")

#Приклад 2
def is_anagram(text1, text2):
    text1 = text1.lower().replace(" ", "")
    text2 = text2.lower().replace(" ", "")
    return sorted(text1) == sorted(text2)

user_input1 = input("Введіть перший текст: ")
user_input2 = input("Введіть другий текст: ")

if is_anagram(user_input1, user_input2):
    print("Це анаграми!")
else:
    print("Це не анаграми.")

#Приклад 3
def calculate_life_number(date):
    date = date.replace(" ", "")  # Видаляємо пробіли з дати

    while len(date) > 1:  # Повторюємо додавання, поки не отримаємо одну цифру
        total = sum(int(digit) for digit in date)
        date = str(total)

    return int(date)

user_input = input("Введіть дату народження (у форматі РРРГММДД, або РРРРДДММ, або ММДДРРРР): ")

life_number = calculate_life_number(user_input)
print("Цифра життя для введеної дати:", life_number)

#Приклад 4
while True:
    try:
        number = int(input("Введіть ціле число: "))
        print(number / 2)
        break
    except ValueError:
        print("Введене значення не є допустимим числом. Повторіть спробу...")

#Завдання 1

def is_hidden(word, combination):
    current_index = -1

    for char in word:
        current_index = combination.find(char, current_index + 1)
        if current_index == -1:
            return False

    return True

word = input("Введіть слово: ")
combination = input("Введіть комбінацію символів: ")

if is_hidden(word, combination):
    print("Yes")
else:
    print("No")

#Завдання 2

def calculate_life_number(date):
    date = date.replace(" ", "")  # Видаляємо пробіли з дати

    try:
        while len(date) > 1:  # Повторюємо додавання, поки не отримаємо одну цифру
            total = sum(int(digit) for digit in date)
            date = str(total)
    except ValueError:
        print("Невірний формат дати. Повторіть спробу...")
        return None

    return int(date)

user_input = input("Введіть дату народження (у форматі РРРГММДД, або РРРРДДММ, або ММДДРРРР): ")

life_number = calculate_life_number(user_input)
if life_number is not None:
    print("Цифра життя для введеної дати:", life_number)

#Завдання 3
