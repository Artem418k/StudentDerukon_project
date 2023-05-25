#Завдання 1
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

test_years = [2000, 2020, 1900, 2024, 2100]
expected_results = [True, True, False, True, False]

for year, expected in zip(test_years, expected_results):
    result = is_leap_year(year)
    if result == expected:
        print(f"Year {year} is a leap year: {result}")
    else:
        print(f"Year {year} is not correctly classified as a leap year. Expected: {expected}, Actual: {result}")

#Завдання 2
def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    # Check if the arguments are valid
    if month < 1 or month > 12:
        return None

    # Define the number of days in each month
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Handle leap year for February
    if month == 2 and is_year_leap(year):
        return 29

    # Return the number of days for the given month
    return month_days[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

#Завдання 3
def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    # Check if the arguments are valid
    if month < 1 or month > 12:
        return None

    # Define the number of days in each month
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Handle leap year for February
    if month == 2 and is_year_leap(year):
        return 29

    # Return the number of days for the given month
    return month_days[month - 1]

def day_of_year(year, month, day):
    # Check if the arguments are valid
    if month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None

    # Calculate the day of the year
    day_count = 0
    for m in range(1, month):
        day_count += days_in_month(year, m)
    day_count += day

    return day_count

print(day_of_year(2000, 12, 31))

#Завдання 4
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

#Завдання 5
def liters_100km_to_miles_gallon(liters):
    miles = 235.215 / liters
    return miles

def miles_gallon_to_liters_100km(miles):
    liters = 235.215 / miles
    return liters

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

#Завдання 6
def is_a_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False

# Приклади використання функції
print(is_a_triangle(3, 4, 5))  # True
print(is_a_triangle(1, 2, 4))  # False
print(is_a_triangle(5, 9, 13))  # True

#Завдання 7
def is_a_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False

def is_a_right_triangle(a, b, c):
    if is_a_triangle(a, b, c):
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            return True
    return False

# Приклади використання функції
print(is_a_right_triangle(3, 4, 5))  # True
print(is_a_right_triangle(5, 12, 13))  # True
print(is_a_right_triangle(4, 7, 9))  # False
print(is_a_right_triangle(8, 15, 17))  # True