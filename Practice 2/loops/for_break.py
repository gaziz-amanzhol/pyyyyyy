#for loop and break the basic
x=int(input())
for i in range(x):
    if(i==13):
        break
    print(i,end=" ")

print(end="\n")

y="Penaldy"
for i in y:
    if i=="a":
        break
    print(i,end="")

print(end="\n")

#some basic example
for i in range(1,11):
    if i%7==0:
        break
    print(i,end=" ")
