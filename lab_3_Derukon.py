#Завдання 1
import math

def gaussian_function(x, mu, sigma):
    coefficient = 1 / math.sqrt(2 * math.pi * sigma**2)
    exponent = -(x - mu)**2 / (2 * sigma**2)
    result = coefficient * math.exp(exponent)
    return result

# Приклад виклику функції зі значеннями x = 1, mu = 0 і sigma = 1
x = 1
mu = 0
sigma = 1
gaussian_value = gaussian_function(x, mu, sigma)
print("Значення функції Гауса:", gaussian_value)


#Завдання 2
john = 3
mary = 5
adam = 6

print(f"{john}, {mary}, {adam}\n")

totalApple = sum([john, mary, adam])
print(f"{totalApple}\n")

print("Загальна кількість яблук:", totalApple)

#Завдання 3
kilometers = 12.25
miles = 7.38

miles_to_kilometers = round(miles * 1.61, 2)
kilometers_to_miles = round(kilometers / 1.61, 2)

print(f"{miles} miles is {miles_to_kilometers} kilometers\n")
print(f"{kilometers} kilometers is {kilometers_to_miles} miles\n")

#Завдання 4
x = float(input("Введіть х: "))
y = 3 * x ** 3 - 2 * x ** 2 + 3 ** x - 1
print(y)

#Завдання 5
# This program computes the number of seconds in a given number of hours

hours = 2  # Number of hours
seconds_per_hour = 3600  # Number of seconds in 1 hour

print("Hours:", hours)  # Printing the number of hours
print("Seconds in Hours:", hours * seconds_per_hour)  # Printing the number of seconds in a given number of hours
print("Goodbye")

# This is the end of the program that computes the number of seconds in 3 hours

#Завдання 6
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))

print("Результат додавання двох чисел дорівнює =", a + b)
print("Результат віднімання двох чисел дорівнює =", a - b)
print("Результат множення двох чисел дорівнює =", a * b)
print("Результат ділення двох чисел дорівнює =", a / b)

print("\nThat's all, folks!")

#Завдання 7
x = float(input("Введіть значення x: "))

# Обчислення виразу
y = 1 / (x + 1 / (x + 1 / (x + 1 / (x + 1 / x))))

# Виведення результату
print("Результат виразу:", y)

#Завдання 8
hour = int(input("Початковий час (години): "))
mins = int(input("Початковий час (хвилини): "))
dura = int(input("Тривалість події (хвилини): "))

# Обчислюємо загальну кількість хвилин
total_mins = hour * 60 + mins + dura

# Обчислюємо години та хвилини закінчення події
end_hour = (total_mins // 60) % 24
end_mins = total_mins % 60

# Форматуємо рядки з годинами та хвилинами для відображення двоцифрового формату
end_hour_str = str(end_hour).zfill(2)
end_mins_str = str(end_mins).zfill(2)

# Виводимо результат
print("Подія закінчується о", end_hour_str, ":", end_mins_str)