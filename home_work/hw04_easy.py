# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
my_list = [1, 2, 4, 0]
my_new_list = [i * i for i in my_list]

print(my_new_list)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
list_1 = ["Апельсин", "Яблоко", "Ананас", "Груша"]
list_2 = ["Киви", "Апельсин", "Вишня", "Яблоко"]
result=list(set(list_1) & set(list_2))
print(result)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
my_list = []
my_new_list = []
for _ in range(10):
    my_list.append(random.randint(-10,10))
for i in my_list:
    if i>=0 and not i%3 and i%4:
        my_new_list.append(i)


print(my_list)
print(my_new_list)

# # Получим нужные данные из лога, для дальнейшего анализа
# log = [
# '64 bytes from localhost.localdomain (127.0.0.1): '
# 'icmp_req=1 ttl=64 time=0.033 ms',
# '64 bytes from localhost.localdomain (127.0.0.1): '
# 'icmp_req=2 ttl=64 time=0.034 ms',
# '64 bytes from localhost.localdomain (127.0.0.1): '
# 'icmp_req=3 ttl=64 time=0.031 ms',
# '64 bytes from localhost.localdomain (127.0.0.1): '
# 'icmp_req=4 ttl=64 time=0.031 ms']
#
# pattern = re.compile('(icmp_req=[\d]+).*(time=[\d\.]+ ms)')
# result = []
# for line in log:
#     result.append(pattern.search(line).groups())
# print(result)
# # Извлечём из html-кода только теги
# html = '<p style="margin-left:10px;">text' \
# '<b class="super-bold">bold text</b>.</p>'
# pattern = '<[^>]+>'
# print(re.findall(pattern, html))