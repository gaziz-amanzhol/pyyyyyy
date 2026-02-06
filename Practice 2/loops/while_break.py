#while_break the basic 
x=int(input())
sum=i=0
while(i<x):
    if(i==12):
        break
    i+=1
    print(i,end=" ")

print(end="\n")

#some basic example

#all divisors to 2
n=int(input())
num=1
while (num<=n):
    print(num,end=" ")
    num*=2
    if(num>n):
        break
