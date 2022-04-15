 #1 --Напишите функцию Python, которая принимает последовательность чисел и определяет, отличаются ли все числа друг от друга.--
 # -- Сандар тізбегін қабылдайтын және барлық сандардың бір-бірінен ерекшеленетінін анықтайтын Python функциясын жазыңыз.--
 # -- Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.--

def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;
print(test_distinct([1,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))

#2 --Напишите программу на Python для создания всех возможных строк с помощью "a", "e", "i", "o", "u". Используйте символы ровно один раз.--
# --Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.--

import random
char_list = ['a','e','i','o','u']
random.shuffle(char_list)
print(''.join(char_list))

#2-2

import itertools
a = [[10, 20], [30, 40], [50]]
for j in (itertools.chain.from_iterable(a)):
   print(j)
print(list(itertools.chain.from_iterable(a)))

print("======================")
#3--Напишите программу на Python для удаления и печати каждого третьего числа из списка чисел, пока список не станет пустым.--
#--Тізім бос болғанша сандар тізімінен әр үшінші санды жою және басып шығару үшін Python бағдарламасын жазыңыз.--
#--The following tool visualize what the computer is doing step-by-step as it executes the said program:--

def remove_nums(int_list):
  #list starts with 0 index
  position = 3 - 1
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)


#Напишите функцию Python для суммирования всех чисел в списке
def sum(numbers):
   total = 0
   for x in numbers:
     total += x
   return total
print(sum((8, 2, 3, 0, 7)))
#4-- Напишите программу на Python, чтобы получать главные новости из новостей Google.
#Write a Python program to get the top stories from Google news.
#
# import bs4
# from bs4 import BeautifulSoup as soup
# from urllib.request import urlopen
#
# news_url="https://news.google.com/news/rss"
# Client=urlopen(news_url)
# xml_page=Client.read()
# Client.close()
#
# soup_page=soup(xml_page,"xml")
# news_list=soup_page.findAll("item")
# # Print news title, url and publish date
# for news in news_list:
#   print(news.title.text)
#   print(news.link.text)
#   print(news.pubDate.text)
#   print("-"*60)

print("======================")
# Write a Python program to get a list of locally installed Python modules.
# Напишите программу на Python, чтобы получить список локально установленных модулей Python.

import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
for m in installed_packages_list:
    print(m)

#Напишите функцию Python, чтобы проверить, является ли строка панграммой или нет.
# Примечание : Панграммы-это слова или предложения, содержащие каждую букву алфавита по крайней мере один раз.
# Например : "Быстрая бурая лиса перепрыгивает через ленивую собаку".
# Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
     alphaset = set(alphabet)
     return alphaset <= set(str1.lower())

print(ispangram('The quick brown fox jumps over the lazy dog'))

