
__author__ = 'Юрченко Андрей Константинович'

# Задача-1: Дано произвольное целое число, вывести поочередно цифры исходного числа

# код пишем тут...
a = 24
i = 1
while i<a:
    print(i)
    i += 1
# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
a = input('Введите первое число: a=')
b = input('Введите второе число: b=')
print('поменяем их местами')
A = b
B = a
print('a='+A)
print('b='+B)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
age = int(input('Сколько вам лет? Введите ваш возраст:'))
if age>=18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')