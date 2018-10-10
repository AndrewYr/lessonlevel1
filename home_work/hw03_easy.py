# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# колхоз конечно, но работает, потом понял что можно сделать было и по другому немного, но не успеваю(
def my_round(number, ndigits):
    dot = str(number).find('.')
    h = int(str(number)[:str(number).find('.')])
    shot = str(number)[dot+1:ndigits+dot+2]
    shot = shot[::-1]

    i = 0
    x=0
    while i < len(shot):
        if i == len(shot)-1 and int(shot[i]) == 9:
            x=1
        if int(shot[i]) > 4:
            shot = shot[:i] + '0' + shot[i + 1:]
        else:
            shot = shot[:i] + str(int(shot[i])+1) + shot[i + 1:]
            break
        i+=1
    shot = str(int(shot[::-1]))
    return float(str(int(number)+x)+'.'+shot[:ndigits])



print(my_round(2.1234967, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


# Колхоз конечно, и на python так писать не нужно, но чтото по другому я не придумал
def lucky_ticket(ticket_number):
    if not len(str(ticket_number))%2:
        long = int(len(str(ticket_number))/2)
    else:
        long = int((len(str(ticket_number))-1)/2)
    a = 0;
    for i in str(ticket_number)[:long]:
        a+=int(i)
    b = 0;
    for i in str(ticket_number)[-long:]:
        b+=int(i)

    return 'Счастливый билет' if a==b else 'Не счастливый билет'

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(111222))
