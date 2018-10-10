# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# загуглил и постарался разобраться
def fibonacci(lowerbound, upperbound):
    x = 0
    y = 1
    while x <= upperbound:
        if (x >= lowerbound):
            yield x
        x, y = y, x + y

startNumber = int(input('Введите начальное число'))
endNumber = int(input('Введите конечное число'))
for fib_sequence in fibonacci(startNumber, endNumber):
    print ("Следующее число %d!" % fib_sequence)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


# скопировал с гугла и постарался разобраться
def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
flt=[]
for i in mixed:
    if i == 'мак':
        flt.append(i)
print(flt)


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# Я не знаю как решить эту задачу и гугул мне не смог помочь(