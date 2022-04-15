N = int(input())

num = 1

while num <= N:

   num *= 2

   if num == N:

       print("YES")

       break

else:

   print("NO")