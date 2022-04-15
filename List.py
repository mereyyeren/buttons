#Напишите программу на Python для суммирования всех элементов в списке.
#Write a Python program to sum all the items in a list.

def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))

#Write a Python program to multiply all the items in a list.
#Напишите программу на Python для умножения всех элементов в списке.

def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,-8]))

#Напишите программу на Python, чтобы получить наибольшее число из списка.
#Write a Python program to get the largest number from a list.

def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))

#Напишите программу на Python, чтобы получить наименьшее число из списка.
#Write a Python program to get the smallest number from a list.

def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(smallest_num_in_list([1, 2, -8, 0]))

#Write a Python program to count the number of strings where the string length is 2 or more and
# the first and last character are same from a given list of strings.
#Напишите программу на Python для подсчета количества строк, длина которых равна 2 или более,
# а первый и последний символ одинаковы из заданного списка строк.
def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))
#Напишите программу на Python для получения списка, отсортированного в порядке возрастания по
# последнему элементу в каждом кортеже из заданного списка непустых кортежей.
# примерный список : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# ожидаемый результат : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
#Write a Python program to get a list, sorted in increasing order by the last element in each
# tuple from a given list of non-empty tuples.
def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
#Напишите программу на Python для удаления дубликатов из списка
#Write a Python program to remove duplicates from a list.
a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)
#Напишите программу на Python для удаления дубликатов из списка.
#Write a Python program to remove duplicates from a list.
a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)
#Напишите программу на Python для печати указанного списка после удаления 0-го, 4-го и 5-го элементов.
#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

#Напишите программу на Python для создания 3*4*6 3D массив, каждый элемент которого равен *.
#Write a Python program to generate a 3*4*6 3D array whose each element is *.
array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)
#Напишите программу на Python, чтобы найти список слов, длина которых превышает n, из заданного списка слов.
#Write a Python program to find the list of words that are longer than n from a given list of words.
def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
print(long_words(3, "The quick brown fox jumps over the lazy dog"))
#Напишите программу на Python для создания и печати списка из первых и последних 5 элементов, значения которых
# представляют собой квадраты чисел от 1 до 30 (оба включены).
#Write a Python program to generate and print a list of first and last 5 elements where the values are square
# of numbers between 1 and 30 (both included).
def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

printValues()
#Напишите программу на Python, чтобы сгенерировать все перестановки списка в Python.
# В математике понятие перестановки относится к акту упорядочения всех членов множества в некоторой
# последовательности или порядке, или, если множество уже упорядочено, перестановки (переупорядочения) его элементов, процессу,
# называемому перестановкой. Они отличаются от комбинаций, которые являются выборками
# некоторых членов набора, где порядок игнорируется.
# Write a Python program to generate all permutations of a list in Python.
# In mathematics, the notion of permutation relates to the act of arranging all the members of a
# set into some sequence or order, or if the set is already ordered, rearranging (reordering) its elements,
# a process called permuting. These differ from combinations, which are selections of some members of a set where order is disregarded.
import itertools
print(list(itertools.permutations([1,2,3])))
#Напишите программу на Python для клонирования или копирования списка
#Write a Python program to clone or copy a list.
original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)
