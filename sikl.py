# #1. Цикл for
# i = 1
# for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
#     print('#', i, ' color of rainbow is ', color, sep = '')
#     i += 1
# #2
# for i in 1, 2, 3, 'one', 'two', 'three':
#     print(i)
#
# #2. Функция range
# for i in range(4):  # равносильно инструкции for i in 0, 1, 2, 3:
#     # здесь можно выполнять циклические действия
#     print(i)
#     print(i ** 2)
# # цикл закончился, поскольку закончился блок с отступом
# print('Конец цикла')
#
# #2.2
# sum = 0
# n = 5
# for i in range(1, n + 1):
#     sum += i
# print(sum)
#
# #3. Настройка функции print()
# print(1, 2, 3)
# print(4, 5, 6)
# print(1, 2, 3, sep=', ', end='. ')
# print(4, 5, 6, sep=', ', end='. ')
# print()
# print(1, 2, 3, sep='', end=' -- ')
# print(4, 5, 6, sep=' * ', end='.')
#
# #Например, следующий фрагмент программы напечатает
# # на экран квадраты всех целых чисел от 1 до 10. Видно, что цикл while может заменять цикл for ... in range(...):
# i = 1
# while i <= 10:
#     print(i ** 2)
#     i += 1
#
# #Вот еще один пример использования цикла while для определения количества цифр натурального числа n:
# n = int(input())
# length = 0
# while n > 0:
#     n //= 10  # это эквивалентно n = n // 10
#     length += 1
# print(length)
#
# #2. Инструкции управления циклом
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# else:
#     print('Цикл окончен, i =', i)
#
# #Приведем пример программы, которая считывает числа до тех пор, пока не встретит отрицательное число. При появлении отрицательного числа
# # программа завершается. В первом варианте последовательность чисел завершается числом 0 (при считывании которого надо остановиться).
# a = int(input())
# while a != 0:
#     if a < 0:
#         print('Встретилось отрицательное число', a)
#         break
#     a = int(input())
# else:
#     print('Ни одного отрицательного числа не встретилось')
# #Во втором варианте программы сначала на вход подается количество элементов последовательности, а затем и сами элементы.
# # В таком случае удобно воспользоваться циклом for. Цикл for также может иметь ветку else и содержать инструкции break внутри себя
# n = int(input())
# for i in range(n):
#     a = int(input())
#     if a < 0:
#         print('Встретилось отрицательное число', a)
#         break
# else:
#     print('Ни одного отрицательного числа не встретилось')
#
# #Если инструкции break и continue содержатся внутри нескольких вложенных циклов, то они влияют лишь на исполнение самого внутреннего
# # цикла. Вот не самый интеллектуальный пример, который это демонстрирует:
# for i in range(3):
#     for j in range(5):
#         if j > i:
#             break
#         print(i, j)
#
# #Увлечение инструкциями break и continue не поощряется, если можно обойтись без их использования.
# # Вот типичный пример плохого использования инструкции break (данный код считает количество знаков в числе).
# n = int(input())
# length = 0
# while True:
#     length += 1
#     n //= 10
#     if n == 0:
#         break
# print('Длина числа равна', length)
# #Гораздо лучше переписать этот цикл так:
# n = int(input())
# length = 0
# while n != 0:
#     length += 1
#     n //= 10
# print('Длина числа равна', length)
# #Впрочем, на Питоне можно предложить и более изящное решение:
# n = int(input())
# print('Длина числа равна', len(str(n)))
# #3. Множественное присваивание
# a = 1
# b = 2
# tmp = a
# a = b
# b = tmp
# print(a, b)
# # 2 1
# #В Питоне то же действие записывается в одну строчку:
# a = 1
# b = 2
# a, b = b, a
# print(a, b)
# # 2 1
#
#
#
# #1. Синтаксис условной инструкции
# x = int(input())
# if x > 0:
#     print(x)
# else:
#     print(-x)
# #2
# x = int(input())
# if x < 0:
#     x = -x
# print(x)
# #3
# x = int(input())
# y = int(input())
# if x > 0:
#     if y > 0:               # x > 0, y > 0
#         print("Первая четверть")
#     else:                   # x > 0, y < 0
#         print("Четвертая четверть")
# else:
#     if y > 0:               # x < 0, y > 0
#         print("Вторая четверть")
#     else:                   # x < 0, y < 0
#         print("Третья четверть")
# #4.1. Логические операторы
# a = int(input())
# b = int(input())
# if a % 10 == 0 or b % 10 == 0:
#     print('YES')
# else:
#     print('NO')
#
# #5. Каскадные условные инструкции
# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print("Первая четверть")
# elif x > 0 and y < 0:
#     print("Четвертая четверть")
# elif y > 0:
#     print("Вторая четверть")
# else:
#     print("Третья четверть")

#
# print("Did Joffrey agree?")
# print("He did. He also said "\I love using\ \\n"")

print("- Did Joffrey agree? \n - He did. He also said "I love using \\n")