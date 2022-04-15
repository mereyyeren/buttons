# # String
# string = "Something"
# name = "mr dj ramo"
# print(name.title())
# print(name.upper())
# print(name.lower())
#
# print("Hello World\nHello Python\n\nHello Everybody")
#
# print("Messages:\n\tHello\n\tPeter")
#
# a = "... rrr ..."
# print(a.rstrip())
# print(a.lstrip())
# print(a.strip())
# a = a.strip(".")
# a = a.strip()
# print(a)
#
# print("--------------------")
#
# # Dictionary
# jihc = {"osp" : "ol senin probleman" , "hayirlisi" : "bari jaqsy bolady"}
# print(jihc)
#
# print((jihc["osp"]))
# print((jihc["hayirlisi"]))
#
# jihc["izin"] = "ruqsat"
# print(jihc)
#
# del jihc["izin"]
# print(jihc)
#
# print(jihc.values())
# print(jihc.keys())
# print(jihc.items())
#
# all_jihc = []
# for i in range(0,10):
#     all_jihc.append(jihc)
#
# for jihc in all_jihc:
#     print(jihc)
#
# print("--------------------")
#
# # Functions
# def factorial(x):
#     n = 1
#     for i in range(1 , x+1):
#         n = n * i
#     return n
# print(factorial(1))
# print(factorial(5))
#
# for i in range(1 , 10):
#     print(str(i) + "!\t = " + str(factorial(i)))
#
# print("--------------------")
#
# # List
# m_list = ["GameDev", "Web", "Java"]
# print(m_list)
# print(len(m_list))
# print(m_list[0])
# m_list[0] = "Photoshop"
# m_list.append("GameDev")
# m_list.insert(2,"HTML")
# print(m_list)
# del m_list[-1]
# print(m_list)
# m_list.remove("Java")
# print(m_list)
# m_list.sort()
# print(m_list)
# m_list.reverse()
# print(m_list)
#
# for x in m_list:
#     print(x.upper())
#
# for r in range(1 , 5):
#     print(r)
#
# n = list(range(0, 5))
# print(n)
#
# for x in n:
#     x = x * 2
#     print(x)
#
# n.sort(reverse=True)
# print(n)
# print(max(n))
# print(min(n))
# print(sum(n))
#
# mylist = m_list[1:3]
# print(mylist)

import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
     alphaset = set(alphabet)
     return alphaset <= set(str1.lower())

print(ispangram('The quick brown fox jumps over the lazy dog'))