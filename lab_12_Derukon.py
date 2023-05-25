# Приклад №1

class Timer:
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def __str__(self):
        return f"{self._format_number(self._hour)}:{self._format_number(self._minute)}:{self._format_number(self._second)}"

    def next_second(self):
        self._second += 1
        if self._second >= 60:
            self._second = 0
            self._minute += 1
            if self._minute >= 60:
                self._minute = 0
                self._hour += 1
                if self._hour >= 24:
                    self._hour = 0

    def prev_second(self):
        self._second -= 1
        if self._second < 0:
            self._second = 59
            self._minute -= 1
            if self._minute < 0:
                self._minute = 59
                self._hour -= 1
                if self._hour < 0:
                    self._hour = 23

    def _format_number(self, number):
        if number < 10:
            return f"0{number}"
        return str(number)


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

#Приклад №2

class WeekDayError(Exception):
    pass

class Weeker:
    _days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day not in self._days_of_week:
            raise WeekDayError
        self._day = day

    def __str__(self):
        return self._day

    def add_days(self, n):
        index = self._days_of_week.index(self._day)
        index = (index + n) % 7
        self._day = self._days_of_week[index]

    def subtract_days(self, n):
        index = self._days_of_week.index(self._day)
        index = (index - n) % 7
        self._day = self._days_of_week[index]

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")

#Приклад №3

import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def distance_from_xy(self, x, y):
        return math.hypot(self._x - x, self._y - y)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))

#Завдання №1
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        side1 = self.__vertices[0].distance_from_point(self.__vertices[1])
        side2 = self.__vertices[1].distance_from_point(self.__vertices[2])
        side3 = self.__vertices[2].distance_from_point(self.__vertices[0])
        return side1 + side2 + side3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())