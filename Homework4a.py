# 1. Вычислить число пи c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# import math
# pi = math.pi

# d = str(input('Введите точность $10^{-1} ≤ d ≤10^{-10}$: '))
# count = 0
# for i in d:
#     count += 1

# if float(d) < 1:
#     pi_rounded = round(pi, count - 2)
# else:
#     pi_rounded = int(round(pi, 0))

# print(f'Число пи, округленное до {d} равно {pi_rounded}')

# 2. Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.
# N = int(input('Введите натуральное число N: '))
# count = 0
# list = []
# for i in range(2, N):
#     if (N % i) == 0:
#         for j in range(2, i):
#             if (i % j) == 0:
#                 count += 1
#         if (count == 0):
#             list.append(i)
#         count = 0
# print(f'Список простых множителей числа {N} это {list}')

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

# def RandList(n):
#     import random
#     l = []
#     for i in range(0, n):
#         l.append(random.randrange(1, 10))
#     return l

# N = int(input('Введите длину последовательности: '))
# list = RandList(N)
# list1 = []
# print(list)

# list1.append(list[0])
# count = 0
# for i in range(1, len(list)):
#     for j in range(0, i):
#         if list[i] == list[j]:
#             count += 1
#     if count == 0:
#         list1.append(list[i])
#     count = 0
# print(f'Неповторяющиеся элементы последовательности {list1}')

# 4. НЕОБЯЗАТЕЛЬНАЯ Задана натуральная степень k. Сформировать случайным
# образом список коэффициентов (значения от 0 до 100) многочлена и записать
# в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# k = int(input('Введите степень k многочлена: '))

# import random
# list = []
# for i in range(1, k + 2):
#     list.append(str(random.randrange(0, 100)))
# # print(list)

# polinom = ''
# if list[k] == '0':
#     polinom_new = polinom.join(str(random.randrange(2, 100)) + '*x**' + str(k))
# elif list[k] == '1':
#     polinom_new = polinom.join('x**' + str(k))
# else:
#     polinom_new = polinom.join(list[k] + '*x**' + str(k))

# for i in range(k - 1, 0, -1):
#     if list[i] == '0':
#         polinom_new = polinom_new + ''
#     elif list[i] == '1':
#         polinom_new = polinom_new + ' + ' + polinom.join('x**' + str(i))
#     elif i == 1:
#         polinom_new = polinom_new + ' + ' + polinom.join(list[i] + '*x')
#     else:
#         polinom_new = polinom_new + ' + ' + polinom.join(list[i] + '*x**' + str(i))

# if list[0] == '0':
#     polinom_new = polinom_new + ''
# else:
#     polinom_new = polinom_new + ' + ' + polinom.join(list[0])
# # print(polinom_new)

# with open ('input.txt', 'w', encoding='utf-8') as file:
#     file.write(polinom_new)

# 5. НЕОБЯЗАТЕЛЬНАЯ Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Сделала без формирования файлов

k1 = int(input('Введите степень первого многочлена: '))
k2 = int(input('Введите степень второго многочлена: '))

def Polinomium(k):
    import random
    list = []
    for i in range(1, k + 2):
        list.append(str(random.randrange(0, 100)))

    polinom = ''
    if list[k] == '0':
        polinom_new = polinom.join(str(random.randrange(2, 100)) + '*x**' + str(k))
    elif list[k] == '1':
        polinom_new = polinom.join('x**' + str(k))
    else:
        polinom_new = polinom.join(list[k] + '*x**' + str(k))

    for i in range(k - 1, 0, -1):
        if list[i] == '0':
            polinom_new = polinom_new + ''
        elif list[i] == '1':
            polinom_new = polinom_new + ' + ' + polinom.join('x**' + str(i))
        elif i == 1:
            polinom_new = polinom_new + ' + ' + polinom.join(list[i] + '*x')
        else:
            polinom_new = polinom_new + ' + ' + polinom.join(list[i] + '*x**' + str(i))

    if list[0] == '0':
        polinom_new = polinom_new + ''
    else:
        polinom_new = polinom_new + ' + ' + polinom.join(list[0])
    
    return polinom_new

polinom1 = Polinomium(k1)
polinom2 = Polinomium(k2)
print()
print(polinom1)
print()
print(polinom2)
print()

polinom1 = polinom1.split(" + ")
polinom2 = polinom2.split(" + ")

polinom1 = polinom1[::-1]
polinom2 = polinom2[::-1]

my_dict1 = {}
for i in range(k1):
    key1 = '*x**' + str(i + 1)
    key12 = 'x**' + str(i + 1)
    for j in polinom1:
        if j.find(key1) >= 0:
            my_dict1[key1[-4:]] = j[:-5]
        elif j.find(key12) >= 0:
            my_dict1[key12] = 1
        elif j.find('*x') >= 0 and len(j) < 5:
            my_dict1['x'] = j[:-2]
        elif len(j) < 3:
            my_dict1[0] = polinom1[0]
    key1 = ''
    key12 = ''

my_dict2 = {}
for i in range(k2):
    key2 = '*x**' + str(i + 1)
    key22 = 'x**' + str(i + 1)
    for j in polinom2:
        if j.find(key2) >= 0:
            my_dict2[key2[-4:]] = j[:-5]
        elif j.find(key22) >= 0:
            my_dict2[key22] = 1
        elif j.find('*x') >= 0 and len(j) < 5:
            my_dict2['x'] = j[:-2]
        elif len(j) < 3:
            my_dict2[0] = polinom2[0]
    key2 = ''
    key22 = ''

my_dict = {}
for i in my_dict1.keys():
    for j in my_dict2.keys():
        if i == j:
            my_dict[i] = str(int(my_dict1[i]) + int(my_dict2[j]))

my_dict = my_dict1 | my_dict
my_dict = my_dict2 | my_dict

my_text = ''
for k, v in my_dict.items():
    if k == 0:
        my_text = my_text + str(v)
    elif v == 1:
        my_text = my_text + ' + ' + str(k)
    else:
        my_text = my_text + ' + ' + str(v) + '*' + str(k)
print(my_text)