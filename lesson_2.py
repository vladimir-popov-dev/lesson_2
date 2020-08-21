'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

i  = 0
for i in range(1, 6):
    print(i, 0)
    i += 1

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''

number = 0
five_times = 0
while number < 10:
    entered_number = int(input('Enter integer number '))
    if entered_number == 5: five_times += 1
    number += 1
print('Entered number five ', five_times,'time(s)')

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

sum = 0
for i in range(1,101):
    sum+=i
print('Sum from 1 to 100 is',sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

mul = 1
for i in range(1,11):
    mul*=i
print('Multiplication from 1 to 10 is',mul)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

integer_number = 2129

while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''

integer_number = 5555
sum = 0
while integer_number>0:
    sum += (integer_number % 10)
    integer_number = integer_number//10
print('Sum of digits of number is',sum)

'''
Задача 7
Найти произведение цифр числа.
'''

integer_number = 222222
mul = 1
while integer_number>0:
    mul *= (integer_number % 10)
    integer_number = integer_number//10
print(mul)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''

integer_number = 22351
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
integer_number = 2927812
max_num = 0
while integer_number>0:
    if max_num < integer_number%10:
        max_num = integer_number % 10
    integer_number //= 10
print('Max number is ',max_num)

'''
Задача 10
Найти количество цифр 5 в числе
'''

integer_number = 2235155555614332154
num_five_count = 0
while integer_number>0:
    if integer_number%10 == 5:
        num_five_count+=1
    integer_number = integer_number//10
print('Number contains five digits',num_five_count, 'times')