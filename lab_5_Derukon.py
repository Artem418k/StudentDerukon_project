#Завдання 1
hat_list = [1, 2, 3, 4, 5]

# Step 1: Prompt the user to replace the middle number
new_number = int(input("Enter a number to replace the middle number: "))
hat_list[2] = new_number

# Step 2: Remove the last element from the list
hat_list.pop()

# Step 3: Print the length of the list
print("Length of the list:", len(hat_list))

print(hat_list)

#Завдання 2
def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

# Приклад використання:
my_list = [4, 2, 7, 1, 9, 5]
print("До сортування:", my_list)

bubble_sort(my_list)

print("Після сортування:", my_list)

#Завдання 3
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Створюємо новий список для зберігання унікальних елементів
unique_list = []

# Перебираємо елементи вихідного списку
for num in my_list:
    # Перевіряємо, чи елемент вже присутній у новому списку
    if num not in unique_list:
        # Якщо елементу немає, додаємо його до нового списку
        unique_list.append(num)

# Виводимо список з унікальними елементами
print("Список з унікальними елементами:")
print(unique_list)

#Завдання 4
# Створення шахівниці 8х8 з пустими клітинками
chessboard = [["_"] * 8 for _ in range(8)]

# Розстановка турів по кутках шахівниці
chessboard[0][0] = "R"  # Ліва верхня клітинка
chessboard[0][7] = "R"  # Права верхня клітинка
chessboard[7][0] = "R"  # Ліва нижня клітинка
chessboard[7][7] = "R"  # Права нижня клітинка

# Виведення шахівниці
for row in chessboard:
    print(" ".join(row))