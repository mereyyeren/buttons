
a=2
b=3
c=a+b
print(c)
print("==========")

# n = int(input())
# print(n+1)

with open('input.txt') as file, open('output.txt', 'w') as out:
    a, b = map(int, file.read().split())
    if a < b:
        x = "<"
    elif a > b:
        x = ">"
    else:
        x = "="

out.write(str(x))