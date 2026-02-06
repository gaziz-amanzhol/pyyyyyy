#while_continue the basic
i = int(input())
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i,end=" ")

print(end="\n")
#some basic example

#divisors of m
n = int(input())
i = 0
m=int(input())
while i < n:
    i += 1
    if i % m == 0:
        continue
    print(i,end=" ")
