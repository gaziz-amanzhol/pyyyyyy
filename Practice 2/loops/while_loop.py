#while the basic 
n = int(input())
i = 1
s = 0
while i <= n:
    if i % 2 == 0:
        s += i
    else:
        s += 0
    i += 1
print(s)
if s > 0:
    print("positive")
else:
    print("zero")
print("done")

#some basic example

#enter 1 to 10
x=1
while x<=10:
    print(x,end=" ")
    x+=1
