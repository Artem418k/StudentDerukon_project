#Завдання №1
def create_tuple(numbers):
    return tuple(numbers)

def filter_numbers(tuple_numbers, n):
    result = [x for x in tuple_numbers if x < n]
    return result

# Введення чисел користувачем
numbers = input("Введіть числа, розділені пробілами: ").split()
numbers = [int(num) for num in numbers]

# Створення кортежу зі списку чисел
tuple_numbers = create_tuple(numbers)

# Введення числа n
n = int(input("Введіть число n: "))

# Фільтрація чисел і виведення результату
result = filter_numbers(tuple_numbers, n)
print("Числа менші за n:", result)


#Завдання №2
def create_tuple(strings):
    return tuple(strings)

def join_strings(tuple_strings):
    joined_string = ', '.join(tuple_strings)
    return joined_string

# Введення рядків користувачем
strings = []
for i in range(3):
    string = input(f"Введіть рядок {i+1}: ")
    strings.append(string)

# Створення кортежу зі списку рядків
tuple_strings = create_tuple(strings)

# З'єднання рядків з комою як роздільником
joined_string = join_strings(tuple_strings)

# Виведення результату
print("З'єднаний рядок:", joined_string)

#Завдання №3
def create_library():
    library = {
        "Книга 1": {
            "Автор": "Автор 1",
            "Рік видання": 2020,
            "Кількість сторінок": 300
        },
        "Книга 2": {
            "Автор": "Автор 2",
            "Рік видання": 2018,
            "Кількість сторінок": 250
        },
        "Книга 3": {
            "Автор": "Автор 3",
            "Рік видання": 2019,
            "Кількість сторінок": 400
        }
    }
    return library

def print_book_info(book_info):
    print("Інформація про книгу:")
    print(f"Автор: {book_info['Автор']}")
    print(f"Рік видання: {book_info['Рік видання']}")
    print(f"Кількість сторінок: {book_info['Кількість сторінок']}")

# Створення словника з інформацією про книги
library = create_library()

# Виведення назв книг
print("Назви книг у бібліотеці:")
for book_title in library.keys():
    print(book_title)

# Введення назви книги користувачем
book_title = input("Введіть назву книги: ")

# Перевірка, чи введена книга є у бібліотеці
if book_title in library:
    book_info = library[book_title]
    print_book_info(book_info)
else:
    print("Книга не знайдена.")

#Завдання №4
def create_students():
    students = {
        "Петров": ("Іван", 20, "Група A"),
        "Сидоров": ("Олексій", 19, "Група B"),
        "Іванова": ("Анна", 21, "Група A"),
        "Смирнов": ("Олег", 18, "Група C")
    }
    return students

def print_student_info(student_info):
    print("Інформація про студента:")
    print(f"Ім'я: {student_info[0]}")
    print(f"Вік: {student_info[1]}")
    print(f"Група: {student_info[2]}")

# Створення словника з інформацією про студентів
students = create_students()

# Виведення прізвищ студентів
print("Прізвища студентів:")
for last_name in students.keys():
    print(last_name)

# Введення прізвища студента користувачем
last_name = input("Введіть прізвище студента: ")

# Перевірка, чи введений студент є у словнику
if last_name in students:
    student_info = students[last_name]
    print_student_info(student_info)
else:
    print("Студент не знайдений.")

#Завдання №5
def add_phone_number(contacts, contact_name, phone_number):
    if contact_name in contacts:
        contacts[contact_name].append(phone_number)
    else:
        contacts[contact_name] = [phone_number]

def print_phone_numbers(contacts):
    for contact_name, phone_numbers in contacts.items():
        print(f"{contact_name}: {phone_numbers}")

# Створення початкового словника контактів
contacts = {
    "Іванов": ["+380971234567", "+380991234567"],
    "Петров": ["+380661234567"],
    "Сидорова": ["+380501234567", "+380681234567", "+380731234567"]
}

# Додавання нових номерів телефонів до контактів
add_phone_number(contacts, "Іванов", "+380931234567")
add_phone_number(contacts, "Петров", "+380631234567")
add_phone_number(contacts, "Сидорова", "+380971234567")

# Виведення списку номерів телефонів для всіх контактів
print_phone_numbers(contacts)